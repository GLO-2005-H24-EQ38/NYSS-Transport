DROP FUNCTION IF EXISTS SearchAccess;
DROP FUNCTION IF EXISTS RetrieveWallet;
DROP PROCEDURE IF EXISTS AddAccess;

DELIMITER //

CREATE FUNCTION SearchAccess (
    p_company_name VARCHAR(100),
    p_access_name VARCHAR(100),
    p_price FLOAT
)
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    DECLARE p_access_list VARCHAR(10000);

    -- Initialize the access list
    SET p_access_list = '';

    -- Concatenate access details to the access list
    SELECT GROUP_CONCAT(
        CONCAT('(', a.id, ', "', a.name, '", ', a.price, ', "', a.type, '", ', a.duration, ')', '\n')
        SEPARATOR ''
    ) INTO p_access_list
    FROM access a
    WHERE (p_company_name IS NULL OR a.company = p_company_name)
        AND (p_access_name IS NULL OR a.name = p_access_name)
        AND (p_price IS NULL OR a.price = p_price);

    RETURN p_access_list;
END //

CREATE FUNCTION RetrieveWallet(
    p_email VARCHAR(100)
)
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    DECLARE wallet_info VARCHAR(10000);

    -- Initialize the wallet_info
    SET wallet_info = '';

    -- Retrieve access information for the user
    SELECT GROUP_CONCAT(
        CONCAT('Access: ', a.name, ', Expiration Date: ', t.expirationDate, ', Access Number: ', t.accessNumber, ', Transaction Date: ', t.transactionDate, ', Transaction Number: ', t.transactionNumber, '\n')
        SEPARATOR ''
    ) INTO wallet_info
    FROM transaction t
    JOIN access a ON t.accessId = a.id
    WHERE t.user = p_email;

    RETURN wallet_info;
END //

CREATE PROCEDURE AddAccess(
    -- TODO Confirmer que l'access_id est donné (généré déjà par l'api)--
    IN p_access_id integer,
    IN p_access_name VARCHAR(100),
    IN p_price FLOAT,
    IN p_company_name VARCHAR(100),
    IN p_access_type enum('ticket','subscription'),
    IN p_duration INT
)
BEGIN
    INSERT INTO company (name) VALUES (p_company_name);
    INSERT INTO access (id, name, price, company, type, duration)
    VALUES (p_access_id, p_access_name, p_price, p_company_name, p_access_type, p_duration);
END //
DELIMITER ;

-- TODO remove them eventually (sample data to check my methods)
 -- Inserting sample data into the company table
 INSERT INTO company (name) VALUES ('Company XYZ');
 INSERT INTO company (name) VALUES ('Company ABC');

 -- Inserting sample data into the access table
 INSERT INTO access (id, name, price, company, type, duration) VALUES (1,'Access 1', 20.00, 'Company XYZ', 'ticket', 3);
 INSERT INTO access (id,name, price, company, type, duration) VALUES (2,'Access 2', 30.00, 'Company XYZ', 'subscription', 5);
 INSERT INTO access (id,name, price, company, type, duration) VALUES (3,'Access 3', 40.00, 'Company ABC', 'ticket', 7);
 INSERT INTO access (id,name, price, company, type, duration) VALUES (4,'Access 4', 50.00, 'Company ABC', 'subscription', 8);

 -- Inserting sample data into the user table
 INSERT INTO user (email, name, password, address, birthday, phone, role)
 VALUES ('user1@example.com', 'User One', 'password123', '123 Main St', '1990-01-01', 1234567890, 'commuter'),
        ('admin@example.com', 'Admin One', 'adminpass', '456 Admin Rd', '1985-05-05', 9087654321, 'admin');

 -- Inserting sample data into the creditCard table
 INSERT INTO creditCard (number, holderName, expirationDate)
 VALUES (1234567890123456, 'User One', '12/25'),
        (9876543210987654, 'Admin One', '11/24');

 -- Inserting sample data into the company table
 INSERT INTO company (name) VALUES ('Company A'), ('Company B');

 -- Inserting sample data into the access table
 INSERT INTO access (id, name, price, company, type, duration)
 VALUES (5, 'Access One', 10.00, 'Company A', 'ticket', 30),
        (6, 'Access Two', 20.00, 'Company B', 'subscription', 14);

 -- Inserting sample data into the commuter table
 INSERT INTO commuter (user, creditCard)
 VALUES ('user1@example.com', 1234567890123456);

 -- Inserting sample data into the admin table
 INSERT INTO admin (user, code, company)
 VALUES ('admin@example.com', 1234, 'Company A');

 -- Inserting sample data into the ticket table
 INSERT INTO ticket (access, passes)
 VALUES (1, 5);

 -- Inserting sample data into the subscription table
 INSERT INTO subscription (access, start)
 VALUES (2, '2024-01-01');

 -- Inserting sample data into the transaction table
 INSERT INTO transaction (accessNumber, transactionNumber, creditCard, user, accessId, transactionDate, expirationDate)
 VALUES (1, 123, 1234567890123456, 'user1@example.com', 1, '2024-03-29', '2024-03-30'),
        (2, 456, 9876543210987654, 'user1@example.com', 2, '2024-03-29', '2024-04-29');

