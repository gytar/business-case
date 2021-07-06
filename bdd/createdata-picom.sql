CREATE DATABASE IF NOT EXISTS PiCom;

use PiCom;

CREATE TABLE IF NOT EXISTS users
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT ,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    phone VARCHAR(50),
    is_admin TINYINT(1)
);

CREATE TABLE IF NOT EXISTS adverts
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT, 
    picture VARCHAR(255),
    date_ad DATE,
    duration INT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS area
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    price FLOAT
);
CREATE TABLE IF NOT EXISTS screen
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(255),
    ip_addr VARCHAR(15),
    area_id INT NOT NULL,
    FOREIGN KEY (area_id) REFERENCES area(id)
);

CREATE TABLE IF NOT EXISTS timetable
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    beginning_time VARCHAR(5),
    end_time VARCHAR(5),
    percentage FLOAT
);

CREATE TABLE IF NOT EXISTS transactions
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    price FLOAT
);

CREATE TABLE IF NOT EXISTS diffusion
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    advert_id INT NOT NULL,
    transaction_id INT NOT NULL,
    area_id INT NOT NULL,
    timetable_id INT NOT NULL,
    FOREIGN KEY (advert_id) REFERENCES adverts(id),
    FOREIGN KEY (transaction_id) REFERENCES transactions(id),
    FOREIGN KEY (area_id) REFERENCES area(id),
    FOREIGN KEY (timetable_id) REFERENCES timetable(id)
);