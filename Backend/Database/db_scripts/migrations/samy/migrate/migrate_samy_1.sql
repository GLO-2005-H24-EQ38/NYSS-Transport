DELIMITER //

CREATE PROCEDURE addCreditcard(IN holder varchar(100), IN cardNumber INTEGER, IN expiration varchar(5),IN userEmail varchar(100))
BEGIN
    IF NOT EXISTS (SELECT * FROM commuter WHERE user = userEmail) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User does not exist';
    END IF;

    IF NOT EXISTS (SELECT * FROM creditCard WHERE cardNumber = number) THEN

        INSERT INTO creditCard (holderName, Number, expirationDate) VALUES (holder, cardNumber, expiration);
    END IF;

    UPDATE commuter SET creditCard = cardNumber WHERE user = userEmail;

END //

DELIMITER ;


INSERT INTO user (email, name, password, address, birthday, phone) VALUE ('whatever@what.com', 'whatevs', 'IamHash', 'somewhere', '2024-03-26', 1234567890);
INSERT INTO user (email, name, password, address, birthday) VALUE ('yo@yo.com', 'what', 'Hash', 'where', '2024-03-26');

INSERT INTO commuter (user) VALUE ('whatever@what.com');
insert into commuter (user) value ('yo@yo.com');

CALL addCreditcard('whatevs', 1234567890, '12/22', 'whatever@what.com');
CALL addCreditcard('whatevs', 1234567890, '12/22', 'yo@yo.com');