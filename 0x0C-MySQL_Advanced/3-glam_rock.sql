-- Third task
-- Lists all Glam Rock bands ranked by longevity
SELECT band_name, (ifnull(split, 2020)-formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
