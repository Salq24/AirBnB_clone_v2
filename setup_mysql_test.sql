--this prepares a mysql server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--Creates new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--grants select privileges for the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVELEGES;
--grants all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.8 TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
