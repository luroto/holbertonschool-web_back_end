-- Second task
--Orders country origins og bands based on number of non unique fans
SELECT origin, sum(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;