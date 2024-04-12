DROP FUNCTION IF EXISTS BuyAccess;
DROP PROCEDURE IF EXISTS DeleteAccess;

DELIMITER //
CREATE FUNCTION BuyAccess(
    quantity INT,
    transaction_number INT,
    p_email VARCHAR(100),
    p_access_id INT
)
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN

DECLARE access_bought_info VARCHAR(10000);

-- Declare variables for access details
DECLARE access_name VARCHAR(100);
DECLARE access_price FLOAT;
DECLARE access_type ENUM('ticket', 'subscription');
DECLARE access_company VARCHAR(100);
DECLARE access_number VARCHAR(36);
DECLARE access_expire_date DATE;
DECLARE access_duration INT;

-- Declare variables for credit card details
DECLARE credit_card_number BIGINT;

-- Check if access is not suspended
IF ( SELECT suspended FROM access WHERE id = p_access_id AND suspended = TRUE) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Access is suspended';
END IF;


-- Retrieve access details
SELECT A.name, A.price, A.type, A.duration, A.company
FROM access A
WHERE A.id = p_access_id AND suspended = FALSE
INTO access_name, access_price, access_type, access_duration, access_company;

-- generate access number
SET access_number = UUID();

-- check if user has a credit card
SELECT creditCard FROM commuter WHERE user = p_email INTO credit_card_number;
IF credit_card_number IS NULL THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'User does not have a credit card';
END IF;

SET access_expire_date = DATE_ADD(CURDATE(), INTERVAL access_duration DAY);

INSERT INTO transaction (accessNumber, transactionNumber, creditCard, user, accessId, transactionDate, expirationDate)
    VALUES (access_number, transaction_number, credit_card_number, p_email, p_access_id, CURDATE(), access_expire_date);

-- Concatenate access details to the access_bought as a JSON object
SET access_bought_info = CONCAT('{name: ', access_name, ', price: ', access_price, ', type: ', access_type,
    ', duration: ', access_duration, ', company: ', access_company, ', access_number: ', access_number,
    ', expiration_date: ', access_expire_date, ', transaction_number: ', transaction_number,'}');

RETURN access_bought_info;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE DeleteAccess(IN p_access_id INT)
BEGIN
    DECLARE accessDuration INT;
    DECLARE deleteDate DATE;

    IF NOT EXISTS (SELECT * FROM access WHERE id = p_access_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Access does not exist';
    END IF;

    SELECT duration FROM access WHERE id = p_access_id INTO accessDuration;

    SET deleteDate = DATE_ADD(CURDATE(), INTERVAL accessDuration DAY);

    INSERT INTO suspendedaccess(access,deletionDate) VALUES (p_access_id, deleteDate);

    UPDATE access SET suspended = TRUE WHERE id = p_access_id;

END //
DELIMITER ;


-- example of a transaction with credit card present
SET @transaction_number = 1;
SET @p_email = 'user1@example.com';
SET @result = BuyAccess(1, @transaction_number, @p_email, 1);

-- example of a transaction with missing credit card (should fail and throw an error)
-- SET @transaction_number = 2;
-- SET @p_email = 'emai';
-- SET @result = BuyAccess(1, @transaction_number, @p_email, 1);

CALL DeleteAccess(1);


