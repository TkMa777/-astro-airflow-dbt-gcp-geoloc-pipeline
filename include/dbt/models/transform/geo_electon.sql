CREATE TABLE geo_electon AS

WITH geo_electon_temp AS (
    SELECT
        position,             
        libelle_departement,
        latitude,             
        longitude             
    FROM {{ source('geo_loc', 'loc_fr_entiere') }}  
    WHERE position IS NOT NULL  
),


joined_data AS (
   
    SELECT
        tmp.position,         
        tmp.libelle_departement,  
        tmp.latitude,             
        tmp.longitude,            
        cr.*                    
    FROM geo_electon_temp tmp  
    LEFT JOIN {{ source('geo_loc', 'complet_region') }} cr ON tmp.libelle_departement = cr.nom_departement
)

SELECT * FROM joined_data;
