DELIMITER //

CREATE PROCEDURE addCreditcard(IN holder varchar(100), IN cardNumber INT(10), IN expiration varchar(5),IN userEmail varchar(100))
BEGIN
    IF NOT EXISTS (SELECT * FROM Creditcard WHERE cardNumber = number) THEN
        INSERT INTO Creditcard (holderName, Number, expirationDate) VALUES (holder, cardNumber, expiration);
    END IF;

    UPDATE commuter SET creditCard = cardNumber WHERE userEmail = user;

END //

DELIMITER ;


INSERT INTO user (email, name, password, address, birthday, phone) VALUE ('whatever.com', 'whatevs', 'IamHash', 'somewhere', '2024-03-26', 1234567890);
INSERT INTO user (email, name, password, address, birthday) VALUE ('yo.com', 'what', 'Hash', 'where', '2024-03-26');

INSERT INTO commuter (user) VALUE ('whatever.com');
insert into commuter (user) value ('yo.com');

CALL addCreditcard('whatevs', 1234567890, '12/22', 'whatever.com');
CALL addCreditcard('whatevs', 1234567890, '12/22', 'yo.com');