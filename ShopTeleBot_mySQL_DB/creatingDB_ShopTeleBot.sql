-- SHOW DATABASES;
-- CREATE DATABASE shoptelebot;
use shoptelebot;
SHOW TABLES;

-- DROP TABLE Orders;
-- DROP TABLE Products;
-- DROP TABLE Categories;
-- DROP TABLE Images;
-- DROP TABLE Users;

SELECT prod_name FROM Products WHERE categories_id IN (SELECT id from Categories WHERE cat_name = "Ключница");

SELECT * from Categories;
SELECT * from Users;
SELECT * from Images;
SELECT * from Products;
SELECT * from Orders;

DELETE FROM Users WHERE chatId = 369698997;