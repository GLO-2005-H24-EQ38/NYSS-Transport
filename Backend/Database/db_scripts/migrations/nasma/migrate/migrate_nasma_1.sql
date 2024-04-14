DROP FUNCTION IF EXISTS SearchAccess;
DROP FUNCTION IF EXISTS RetrieveWallet;
DROP FUNCTION IF EXISTS AddAccess;

DELIMITER //

CREATE FUNCTION SearchAccess (
    p_company_name VARCHAR(100),
    p_access_name VARCHAR(100),
    p_access_type FLOAT,
    p_numberOfPassage integer
)
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    DECLARE p_access_list VARCHAR(10000);

    -- Initialize the access list as a JSON array
    SET p_access_list = '';

    -- Concatenate access details to the access list
    SELECT GROUP_CONCAT(
        CONCAT(
            '{"accessId": "', a.id, '",',
            '"accessName": "', a.name, '",',
            '"price": ', a.price, ',',
            '"accessType": "', a.type, '",',
            '"duration": ', a.duration, ',',
            '"company": "', a.company, '"',
            IF(a.type = 'ticket', CONCAT(',"numberOfPassage": ', t.passes), ''),
            '}'
        ) SEPARATOR ','
    ) INTO p_access_list
    FROM access a
    LEFT JOIN ticket t ON a.id = t.access
    WHERE (p_company_name IS NULL OR a.company = p_company_name)
        AND (p_access_name IS NULL OR a.name = p_access_name)
        AND (p_access_type IS NULL OR a.type = p_access_type)
        AND (p_numberOfPassage IS NULL OR t.passes = p_numberOfPassage);

    -- Finalize the JSON array
    SET p_access_list = CONCAT('[',p_access_list, ']');

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
        CONCAT(
            '{"accessNumber": "', t.accessNumber, '",',
            '"accessName": "', a.name, '",',
            '"accessType": "', a.type, '",',
            '"transactionDate": ', t.transactionDate, ',',
            '"expirationDate": ', t.expirationDate, ',',
            '"transactionNumber": "', t.transactionNumber, '"',
            '"company": "', a.company, '"',
            IF(a.type = 'ticket', CONCAT(',"numberOfPassage": ', tk.passes), ''),
            '}'
        ) SEPARATOR ','
    ) INTO wallet_info
    FROM transaction t
    JOIN access a ON t.accessId = a.id
    LEFT JOIN ticket tk ON a.id = tk.access
    WHERE t.user = p_email;

    -- Finalize the JSON array
    SET wallet_info = CONCAT('[', wallet_info, ']');

    RETURN wallet_info;
END //

CREATE FUNCTION AddAccess(
    p_access_id VARCHAR(100),
    p_access_name VARCHAR(100),
    p_price FLOAT,
    p_company_name VARCHAR(100),
    p_access_type enum('ticket','subscription'),
    p_duration INT,
    p_numberOfPassage integer
) RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    DECLARE access_created VARCHAR(10000);
    -- Insertion de la compagnie si elle n'existe pas déjà
    INSERT IGNORE INTO company (name) VALUES (p_company_name);

    -- Insertion dans la table access
    INSERT INTO access (id, name, price, company, type, duration)
    VALUES (p_access_id, p_access_name, p_price, p_company_name, p_access_type, p_duration);

     -- Insertion dans la table appropriée en fonction du type d'accès
    IF p_access_type = 'ticket' THEN
        INSERT INTO ticket (access, passes) VALUES (p_access_id, p_numberOfPassage);
    ELSEIF p_access_type = 'subscription' THEN
        INSERT INTO subscription (access) VALUES (p_access_id);
    END IF;

    SET access_created = CONCAT(
    '{"accessId": "', p_access_id, '",',
    '"accessName": "', p_access_name, '",',
    '"price": "', p_price, '",',
    '"accessType": "', p_access_type, '",',
    '"duration": "', p_duration, '",',
    '"company": "', p_company_name, '"',
    IF(p_access_type = 'ticket', CONCAT(',"numberOfPassage": "', p_numberOfPassage, '"'), ''),
    '}'
);

    RETURN access_created;
END //
DELIMITER ;

-- TODO remove them eventually (sample data to check my methods)
 -- Inserting sample data into the company table
 INSERT INTO company (name) VALUES ('RTC');
 INSERT INTO company (name) VALUES ('STM');

 -- Inserting sample data into the access table
 INSERT INTO access (id, name, price, company, type, duration) VALUES (1,'Access 1', 20.00, 'Company XYZ', 'ticket', 3);
 INSERT INTO access (id,name, price, company, type, duration) VALUES (2,'Access 2', 30.00, 'Company XYZ', 'subscription', 5);
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
 INSERT INTO company (name) VALUES ('RTC'), ('STM');

 -- Inserting sample data into the access table
 INSERT INTO access (id, name, price, company, type, duration)
 VALUES (5, 'Access 5', 10.00, 'RTC', 'ticket', 30),
        (6, 'Access 6', 20.00, 'STM', 'subscription', 14);

 -- Inserting sample data into the commuter table
 INSERT INTO commuter (user, creditCard)
 VALUES ('user1@example.com', 1234567890123456);

 -- Inserting sample data into the admin table
 INSERT INTO admin (user, code, company)
 VALUES ('admin@example.com', 1234, 'RTC');

 -- Inserting sample data into the ticket table
 INSERT INTO ticket (access, passes)
 VALUES (1, 5);

 -- Inserting sample data into the subscription table
 INSERT INTO subscription (access)
 VALUES (2), (4), (5);

 -- Inserting sample data into the transaction table
 INSERT INTO transaction (accessNumber, transactionNumber, creditCard, user, accessId, transactionDate, expirationDate)
 VALUES (1, 123, 1234567890123456, 'user1@example.com', 1, '2024-03-29', '2024-03-30'),
        (2, 456, 9876543210987654, 'user1@example.com', 2, '2024-03-29', '2024-04-29');

