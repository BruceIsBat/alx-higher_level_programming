-- This script creates a table name force_name on MySQL server

data_base=$1;
CREATE DATABASE IF NOT EXISTS data_base;
USE data_base;
CREATE TABLE IF NOT EXISTS force_name (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
