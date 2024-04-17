-- This script creates a table name force_name on MySQL server

USE $1;
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
