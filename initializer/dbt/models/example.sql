SELECT id, name FROM {{ ref('raw_data') }}
WHERE active = true;
