CREATE TABLE user (
    email varchar(100),
    name varchar(100) NOT NULL ,
    password varchar(100) NOT NULL ,
    address varchar(100) NOT NULL ,
    birthday date NOT NULL ,
    phone NUMERIC(10),
    role enum('commuter','admin') DEFAULT 'commuter' NOT NULL ,
    PRIMARY KEY (email),
    CONSTRAINT validEmail CHECK (email LIKE '%@%.%'),
    CONSTRAINT validPhone CHECK (phone > 0)
);

CREATE TABLE creditCard (
    number BIGINT,
    holderName varchar(100) NOT NULL ,
    expirationDate char(5) NOT NULL ,
    PRIMARY KEY (number),
    CONSTRAINT invalidExpirationDate_invalidFormat CHECK (expirationDate LIKE '__/__')
);

CREATE TABLE company (
    name varchar(100),
    PRIMARY KEY (name)
);

CREATE TABLE access (
    id varchar(100),
    name varchar(100) NOT NULL ,
    price float NOT NULL ,
    company varchar(100),
    type enum('ticket','subscription') NOT NULL,
    duration INT NOT NULL,
    suspended BOOLEAN DEFAULT FALSE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (company) REFERENCES company (name) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE commuter(
    user varchar(100),
    creditCard BIGINT ,
    PRIMARY KEY (user),
    FOREIGN KEY (user) REFERENCES user (email) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (creditCard) references creditCard(number) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE admin(
    user varchar(100),
    code varchar(100) NOT NULL ,
    company varchar(100),
    PRIMARY KEY (user),
    FOREIGN KEY (user) REFERENCES user (email) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (company) REFERENCES company (name) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE ticket(
    access varchar(100),
    passes integer NOT NULL,
    PRIMARY KEY (access),
    FOREIGN KEY (access) REFERENCES access (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE subscription (
    access varchar(100),
    PRIMARY KEY (access),
    FOREIGN KEY (access) REFERENCES access (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE transaction (
    accessNumber VARCHAR(36),
    transactionNumber integer NOT NULL,
    creditCard BIGINT NOT NULL,
    user varchar(100) NOT NULL,
    accessId varchar(100) NOT NULL ,
    transactionDate DATE NOT NULL ,
    expirationDate DATE NOT NULL ,
    PRIMARY KEY (accessNumber),
    FOREIGN KEY (user) REFERENCES commuter (user)  ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (creditCard) REFERENCES creditCard (number),
    FOREIGN KEY (accessId) REFERENCES access (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE suspendedAccess (
    access varchar(100),
    deletionDate DATE NOT NULL,
    PRIMARY KEY (access),
    FOREIGN KEY (access) REFERENCES access (id) ON UPDATE CASCADE ON DELETE CASCADE
);


DELIMITER //

CREATE TRIGGER checkExpirationDateBeforeInsert
BEFORE INSERT ON creditCard
FOR EACH ROW
BEGIN
    DECLARE current_month INT;
    DECLARE current_year INT;
    DECLARE card_month INT;
    DECLARE card_year INT;

    SET current_month = MONTH(CURDATE());
    SET current_year = YEAR(CURDATE());
    SET card_month = SUBSTRING(NEW.expirationDate, 1, 2);
    SET card_year = SUBSTRING(NEW.expirationDate, 4, 2);

    IF (card_year < RIGHT(YEAR(NOW()), 2)) OR
       (card_year = RIGHT(YEAR(NOW()), 2) AND card_month < MONTH(NOW())) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Expiration date must be in the future';
    END IF;
END//

DELIMITER ;

DELIMITER //

CREATE EVENT deleteSuspendedAccess
ON SCHEDULE  EVERY 1 DAY STARTS CURDATE() DO
BEGIN
    DECLARE accessId INT;
    DECLARE complete integer DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT access FROM suspendedAccess WHERE deletionDate <= CURDATE();
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET complete = TRUE;

    OPEN  cur;
    deleteAccesses :LOOP
        FETCH cur INTO accessId;
        IF (complete) THEN
            LEAVE deleteAccesses;
        END IF;

        DELETE FROM access WHERE id = accessId;

    end loop deleteAccesses;
    CLOSE cur;
END//

DELIMITER ;

