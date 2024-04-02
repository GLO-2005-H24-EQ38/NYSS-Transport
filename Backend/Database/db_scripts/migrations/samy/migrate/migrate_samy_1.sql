DROP PROCEDURE IF EXISTS addCreditcard;
DROP PROCEDURE IF EXISTS replaceCreditcard;
DROP PROCEDURE IF EXISTS deleteCreditcard;


DELIMITER //

CREATE PROCEDURE addCreditcard(IN holder varchar(100), IN cardNumber BIGINT, IN expiration varchar(5),IN userEmail varchar(100))
BEGIN
     DECLARE oldCardNumber BIGINT;

    IF NOT EXISTS (SELECT * FROM commuter WHERE user = userEmail) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User does not exist';
    END IF;

    SELECT creditCard INTO oldCardNumber FROM commuter WHERE user = userEmail;

    IF NOT EXISTS (SELECT * FROM creditCard WHERE number = cardNumber AND holderName = holder AND expirationDate = expiration) THEN

        INSERT INTO creditCard (holderName, Number, expirationDate) VALUES (holder, cardNumber, expiration);
    END IF;

    UPDATE commuter SET creditCard = cardNumber WHERE user = userEmail;

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

    SELECT creditCard INTO oldCardNumber FROM commuter WHERE user = userEmail;
    UPDATE commuter SET creditCard = NULL WHERE user = userEmail;

    IF NOT EXISTS (SELECT * FROM commuter WHERE creditCard = oldCardNumber) THEN
        DELETE FROM creditCard WHERE number = oldCardNumber;
    END IF;

END //

DELIMITER ;



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


CALL addCreditcard('whatevs', 1234567890, '12/22', 'whatever@what.com'); /*adds credit card and updates commuter*/
CALL addCreditcard('whatevs', 1234567890, '12/22', 'yo@yo.com'); /*only updates commuter*/
CALL addCreditcard('whatevs', 1234567890, '12/22', 'Rando@rand.ran'); /*used in replacement*/
CALL addCreditcard('shouldNotbeThere', 123456789012345, '12/22', 'hello@whatsup.hi');/*used in replacement*/
CALL addCreditcard('whatevs', 1234567890, '12/22', 'yolo@theRealones.real'); /*used in deletion*/
CALL addCreditcard('shouldNotbeThere', 123, '12/22', 'Nocredit@nobitches.L'); /*should not work*/

CALL deleteCreditcard('yolo@theRealones.real'); /*deletes creditCard from commuter*/
CALL deleteCreditcard('Nocredit@nobitches.L'); /*deletes creditCard from commuter and table*/

CALL addCreditcard('Rando', 0123123456789, '13/24', 'Rando@rand.ran'); /* replaces CreditCard without Deletion*/
CALL addCreditcard('whatsup', 12345, '13/24', 'hello@whatsup.hi'); /* replaces CreditCard with Deletion*/
