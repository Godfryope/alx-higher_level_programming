#!/bin/bash

-- script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
mysql -u <username> -p -e "SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='$1' AND TABLE_NAME='first_table'" hbtn_0c_0



