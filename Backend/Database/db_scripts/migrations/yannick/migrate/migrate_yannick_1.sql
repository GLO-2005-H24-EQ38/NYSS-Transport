DROP FUNCTION IF EXISTS BuyAccess;
DROP PROCEDURE IF EXISTS DeleteAccess;
DROP FUNCTION IF EXISTS GetAccessBought;
DROP FUNCTION IF EXISTS GetCreditCard;


DELIMITER //
-- Function to buy access
CREATE FUNCTION BuyAccess(
    quantity INT,
    p_email VARCHAR(100),
    p_access_id VARCHAR(100)
)
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    -- Declare variable to hold access details
    DECLARE access_bought_info VARCHAR(10000);

    -- Declare variables for access details
    DECLARE access_name VARCHAR(100);
    DECLARE access_price FLOAT;
    DECLARE access_type ENUM('ticket', 'subscription');
    DECLARE access_company VARCHAR(100);
    DECLARE access_number VARCHAR(36);
    DECLARE access_expire_date DATE;
    DECLARE access_duration INT;
    DECLARE json_access_bought_info VARCHAR(10000);
    DECLARE transaction_number BIGINT;
    DECLARE number_of_passage INT;

    -- Declare variables for credit card details
    DECLARE credit_card_number BIGINT;

    -- Check if access is not suspended
    IF ( SELECT suspended FROM access WHERE id = p_access_id AND suspended = TRUE) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Access is suspended';
    END IF;

    SET transaction_number = UUID_SHORT();
    SET access_bought_info = '';
    SET json_access_bought_info = '';

    WHILE quantity > 0 DO
            -- Retrieve access details
            SELECT A.name, A.price, A.type, A.duration, A.company
            FROM access A
            WHERE A.id = p_access_id AND suspended = FALSE
            INTO access_name, access_price, access_type, access_duration, access_company;

            -- generate access number
            SET access_number = REPLACE(SUBSTRING(UUID() FROM 1 FOR 13), '-', '');

            -- check if user has a credit card
            SELECT creditCard FROM commuter WHERE user = p_email INTO credit_card_number;
            IF credit_card_number IS NULL THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'User does not have a credit card';
            END IF;

            -- Calculate expiration date
            IF access_type = 'ticket' THEN
                SELECT passes FROM ticket WHERE access = p_access_id INTO number_of_passage;
            END IF;

            -- Calculate expiration date
            SET access_expire_date = DATE_ADD(CURDATE(), INTERVAL access_duration DAY);

            INSERT INTO transaction (accessNumber, transactionNumber, creditCard, user, accessId, transactionDate, expirationDate)
                VALUES (access_number, transaction_number, credit_card_number, p_email, p_access_id, CURDATE(), access_expire_date);

            -- Concatenate access details to the access_bought as a JSON object
            SET access_bought_info = CONCAT(
                    '{"name": "', access_name, '", "price": "', access_price,
                    '", "accessType": "', access_type, '", "company": "', access_company,
                    '", "outOfSale": ',
                      EXISTS(SELECT 1 FROM suspendedAccess sus WHERE sus.access = p_access_id),
                    ', "accessNumber": "', access_number, '", "transactionDate": "', CURDATE(),
                    IF(access_type = 'ticket', CONCAT('", "numberOfPassage": "', number_of_passage), ''),
                    '", "expirationDate": "', access_expire_date, '", "transactionNumber": "', transaction_number,'"}');

            -- Append the current JSON string to the accumulated JSON strings
            SET json_access_bought_info = CONCAT(json_access_bought_info, ',', access_bought_info);

            SET quantity = quantity - 1;
    END WHILE;

    -- Remove the leading comma and add square brackets to make it a valid JSON array
    SET json_access_bought_info = CONCAT('[', SUBSTRING(json_access_bought_info FROM 2), ']');

    RETURN json_access_bought_info;
END //
DELIMITER ;

DELIMITER //
-- Function to get access bought by a user
CREATE FUNCTION GetAccessBought(p_email VARCHAR(100))
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    -- Declare variable to hold bought access details
    DECLARE access_bought_info VARCHAR(10000);

    -- Initialize the access_bought_info
    SET access_bought_info = '';

    -- Retrieve access information for the user
    SELECT GROUP_CONCAT(
        CONCAT(
            '{"accessNumber": "', t.accessNumber, '",',
            '"price": "', a.price, '",',
            '"name": "', a.name, '",',
            '"accessType": "', a.type, '",',
            '"transactionDate": "', t.transactionDate, '",',
            '"expirationDate": "', t.expirationDate, '",',
            '"outOfSale": ', suspended, ',',
            '"deletionDate": "', IF(suspended, CONCAT('"', (SELECT deletionDate FROM suspendedAccess sus WHERE sus.access = a.id), '"'), '0'), '",',
            '"transactionNumber": "', t.transactionNumber, '",',
            IF(a.type = 'ticket', CONCAT('"numberOfPassage": "', tk.passes, '",' ), ''),
            '"company": "', a.company, '"',
            '}'
        ) SEPARATOR ','
    ) INTO access_bought_info
    FROM transaction t
    JOIN access a ON t.accessId = a.id      -- join to get access details
    LEFT JOIN ticket tk ON a.id = tk.access -- join left to handle tickets since ticket have additional information
    WHERE t.user = p_email;

    -- Finalize the JSON array
    SET access_bought_info = CONCAT('[', access_bought_info, ']');

    RETURN access_bought_info;
END //
DELIMITER ;

DELIMITER //
-- Procedure to delete access
CREATE PROCEDURE DeleteAccess(IN p_access_id varchar(100))
BEGIN
    -- Declare variables
    DECLARE accessDuration INT;
    DECLARE deleteDate DATE;

    -- Check if access exists
    IF NOT EXISTS (SELECT * FROM access WHERE id = p_access_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Access does not exist';
    END IF;

    -- Retrieve access duration
    SELECT duration FROM access WHERE id = p_access_id INTO accessDuration;

    -- Calculate deletion date
    SET deleteDate = DATE_ADD(CURDATE(), INTERVAL accessDuration DAY);

    -- Insert into suspendedaccess table
    INSERT INTO suspendedAccess(access,deletionDate) VALUES (p_access_id, deleteDate);

    -- Update access status to suspended
    UPDATE access SET suspended = TRUE WHERE id = p_access_id;

END //
DELIMITER ;

DELIMITER //
-- Function to return credit card information
CREATE FUNCTION GetCreditCard(p_email VARCHAR(100))
RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    -- Declare variables
    DECLARE credit_card_number BIGINT;
    DECLARE credit_card_holder VARCHAR(100);
    DECLARE credit_card_expiration VARCHAR(5);
    DECLARE credit_card_info VARCHAR(10000);

    -- Retrieve credit card information
    SELECT creditCard, holderName, expirationDate
    FROM commuter JOIN creditCard ON commuter.creditCard = creditCard.number
    WHERE user = p_email
    INTO credit_card_number, credit_card_holder, credit_card_expiration;

    -- Construct JSON object for credit card information
    SET credit_card_info = CONCAT('{"cardNumber": "', credit_card_number, '", "holder": "', credit_card_holder,
        '", "expirationDate": "', credit_card_expiration, '"}');

    RETURN credit_card_info;
END //

-- TODO remove thes once data has been added
-- example of a transaction with credit card present
SET @transaction_number = SELECT BuyAccess(1, 'user1@example.com', 2);

-- example of a transaction with missing credit card (should fail and throw an error)
-- SET @transaction_number = 2;
-- SET @p_email = 'emai';
-- SET @result = BuyAccess(1, @transaction_number, @p_email, 1);

CALL DeleteAccess(1);


