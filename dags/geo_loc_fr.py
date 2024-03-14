from datetime import datetime
from airflow.decorators import dag, task

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

from airflow.models.baseoperator import chain

from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType


from include.dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig



@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None, 
    catchup=False, 
    tags=['geo_loc_fr'],
)
def geo_loc_fr():
    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='include/dataset/fr-en-adresse-et-geolocalisation.csv',
        dst='raw/fr_geo.csv',
        bucket='mspr_porc',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )

    create_geo_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_geo_dataset',
        dataset_id='geo_loc',
        gcp_conn_id='gcp',
    )

    gcs_to_raw = aql.load_file(
        task_id='gcs_to_raw',
        input_file=File(
            'gs://mspr_porc/raw/fr-en-adresse-et-geolocalisation.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name='loc_fr_entiere',
            conn_id='gcp',
            metadata=Metadata(schema='geo_loc')
        ),
        use_native_support=False,
    )


    transform = DbtTaskGroup(
        group_id='transform',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_transform(scan_name='check_transform', checks_subpath='transform'):
        from include.soda.check_function import check

        return check(scan_name, checks_subpath)
    


    

    chain(
        upload_csv_to_gcs,
        create_geo_dataset,
        gcs_to_raw,
        transform,
        check_transform(),
    )



geo_loc_fr()    


