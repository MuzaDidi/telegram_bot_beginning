CREATE TABLE Users 
(id serial AUTO_INCREMENT,
chatId INT UNIQUE NOT NULL,
user_name CHAR(50) NOT NULL,
user_firstName CHAR(50) NOT NULL,
user_lastName CHAR(50),
user_phone INT UNIQUE,
user_status CHAR(20) NOT NULL,
PRIMARY KEY (id)) 
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE Categories 
(id serial AUTO_INCREMENT,
cat_name CHAR(50) UNIQUE NOT NULL,
PRIMARY KEY (id)) 
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE Images 
(id serial AUTO_INCREMENT,
img_path CHAR(100) NOT NULL,
img_name CHAR(100) NOT NULL,
PRIMARY KEY (id)) 
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE Products 
(id serial AUTO_INCREMENT,
categories_id BIGINT UNSIGNED  NOT NULL,
prod_name CHAR(50) NOT NULL,
quantity INT NOT NULL,
descrip CHAR(200),
price INT NOT NULL,
images_id BIGINT UNSIGNED  NOT NULL,
FOREIGN KEY (categories_id) REFERENCES Categories (Id) 
ON DELETE RESTRICT ON UPDATE CASCADE,
FOREIGN KEY (images_id) REFERENCES Images (id) 
ON DELETE RESTRICT ON UPDATE CASCADE,
PRIMARY KEY (id)) 
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE Orders 
(id serial AUTO_INCREMENT,
products_id BIGINT UNSIGNED  NOT NULL,
users_id BIGINT UNSIGNED  NOT NULL,
order_status CHAR(20) NOT NULL,
product_count INT,
FOREIGN KEY (products_id) REFERENCES Products (Id) 
ON DELETE RESTRICT ON UPDATE CASCADE,
FOREIGN KEY (users_id) REFERENCES Users (id) 
ON DELETE RESTRICT ON UPDATE CASCADE,
PRIMARY KEY (id)) 
ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;