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

CREATE PROCEDURE deleteCreditcard ( IN userEmail varchar(100))
BEGIN
    DECLARE oldCardNumber BIGINT;

    IF NOT EXISTS (SELECT * FROM commuter WHERE user = userEmail) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User does not exist';
    END IF;

    -- Retrieve the current credit card number of the user
    SELECT creditCard  FROM commuter WHERE user = userEmail INTO oldCardNumber;
    -- Update the user's credit card information to NULL

    UPDATE commuter SET creditCard = NULL WHERE user = userEmail;

    -- Check if the old credit card is not associated with any user
    IF NOT EXISTS (SELECT * FROM commuter WHERE creditCard = oldCardNumber) THEN
        DELETE FROM creditCard WHERE number = oldCardNumber;
    END IF;

END //

DELIMITER ;


-- TODO remove thes once data has been added
INSERT INTO user (email, name, password, address, birthday, phone) VALUE ('whatever@what.com', 'whatevs', 'IamHash', 'somewhere', '2024-03-26', 1234567890);
INSERT INTO user (email, name, password, address, birthday) VALUE ('yo@yo.com', 'what', 'Hash', 'where', '2024-03-26');
INSERT INTO user (email, name, password, address, birthday) VALUE ('Rando@rand.ran', 'what', 'Hash', 'where', '2024-03-26');
INSERT INTO user (email, name, password, address, birthday) VALUE ('hello@whatsup.hi', 'what', 'Hash', 'where', '2024-03-26');
INSERT INTO user (email, name, password, address, birthday) VALUE ('yolo@theRealones.real', 'what', 'Hash', 'where', '2024-03-26');
INSERT INTO user (email, name, password, address, birthday) VALUE ('Nocredit@nobitches.L', 'what', 'Hash', 'where', '2024-03-26');

INSERT INTO commuter (user) VALUE ('whatever@what.com');
INSERT INTO commuter (user) VALUE ('yo@yo.com');
INSERT INTO commuter (user) VALUE ('Rando@rand.ran');
INSERT INTO commuter (user) VALUE ('hello@whatsup.hi');
INSERT INTO commuter (user) VALUE ('yolo@theRealones.real');
INSERT INTO commuter (user) VALUE ('Nocredit@nobitches.L');


CALL addCreditcard('whatevs', 1234567890, '12/32', 'whatever@what.com'); /*adds credit card and updates commuter*/
CALL addCreditcard('whatevs', 1234567890, '12/32', 'yo@yo.com'); /*only updates commuter*/
CALL addCreditcard('whatevs', 1234567890, '12/32', 'Rando@rand.ran'); /*used in replacement*/
CALL addCreditcard('shouldNotbeThere', 123456789012345, '12/32', 'hello@whatsup.hi');/*used in replacement*/
CALL addCreditcard('whatevs', 1234567890, '12/32', 'yolo@theRealones.real'); /*used in deletion*/
CALL addCreditcard('shouldNotbeThere', 123, '12/32', 'Nocredit@nobitches.L'); /*should not work*/

CALL deleteCreditcard('yolo@theRealones.real'); /*deletes creditCard from commuter*/
CALL deleteCreditcard('Nocredit@nobitches.L'); /*deletes creditCard from commuter and CreditCard table*/

CALL addCreditcard('Rando', 0123123456789, '12/24', 'Rando@rand.ran'); /* replaces CreditCard without Deletion*/
CALL addCreditcard('whatsup', 12345, '12/24', 'hello@whatsup.hi'); /* replaces CreditCard with Deletion*/




