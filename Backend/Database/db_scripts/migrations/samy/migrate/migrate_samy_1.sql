DROP PROCEDURE IF EXISTS addCreditcard;
DROP PROCEDURE IF EXISTS replaceCreditcard;
DROP PROCEDURE IF EXISTS deleteCreditcard;


DELIMITER //

-- Procedure to add a credit card to a user's account
CREATE PROCEDURE addCreditcard(IN holder varchar(100), IN cardNumber BIGINT, IN expiration varchar(5),IN userEmail varchar(100))
BEGIN
    -- Declare variable to hold the old card number
    DECLARE oldCardNumber BIGINT;

    -- Check if the user exists
    IF NOT EXISTS (SELECT * FROM commuter WHERE user = userEmail) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User does not exist';
    END IF;

    -- Retrieve the current credit card number of the user
    SELECT creditCard INTO oldCardNumber FROM commuter WHERE user = userEmail;

    -- Check if the new credit card information does not exist in the database
    IF NOT EXISTS (SELECT * FROM creditCard WHERE number = cardNumber AND holderName = holder AND expirationDate = expiration) THEN
        INSERT INTO creditCard (holderName, Number, expirationDate) VALUES (holder, cardNumber, expiration);
    END IF;

    -- Update the user's credit card information with the new card number
    UPDATE commuter SET creditCard = cardNumber WHERE user = userEmail;

    -- Check if the old credit card is not associated with any user
    IF NOT EXISTS (SELECT * FROM commuter WHERE creditCard = oldCardNumber) THEN
        DELETE FROM creditCard WHERE number = oldCardNumber;
    END IF;

END //

DELIMITER ;

DELIMITER //

-- Procedure to delete a user's credit card from their account
CREATE PROCEDURE deleteCreditcard ( IN userEmail varchar(100))
BEGIN
    -- Declare variable to hold the old card number
    DECLARE oldCardNumber BIGINT;

    -- Check if the user exists
    IF NOT EXISTS (SELECT * FROM commuter WHERE user = userEmail) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User does not exist';
    END IF;

    -- Retrieve the current credit card number of the user
    SELECT creditCard FROM commuter WHERE user = userEmail INTO oldCardNumber;
    -- Update the user's credit card information to NULL
    UPDATE commuter SET creditCard = NULL WHERE user = userEmail;

    -- Check if the old credit card is not associated with any user
    IF NOT EXISTS (SELECT * FROM commuter WHERE creditCard = oldCardNumber) THEN
        DELETE FROM creditCard WHERE number = oldCardNumber;
    END IF;

END //

DELIMITER ;

