#!/bin/bash

-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, MAX(temperature) AS max_temp FROM temperatures WHERE MONTH(date) IN (7, 8) GROUP BY city ORDER BY max_temp DESC LIMIT 3

