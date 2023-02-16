#!/bin/bash

-- script that creates the database hbtn_0d_usa and the table states (database hbtn_0d_usa) on your MySQL server.
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);

