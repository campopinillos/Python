-- Script that prepares a MySQL server for the project:
CREATE DATABASE
IF NOT EXISTS flaskcontacts;
CREATE USER
IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `root`.* TO 'root'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON `root`.* TO 'root'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;

USE flaskcontacts;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;

CREATE TABLE `contacts` (
  `id` INT AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;