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
    transactionNumber BIGINT NOT NULL,
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
-- Trigger to check expiration date before inserting a new credit card
CREATE TRIGGER checkExpirationDateBeforeInsert
BEFORE INSERT ON creditCard
FOR EACH ROW
BEGIN
    -- Declare variables
    DECLARE current_month INT;
    DECLARE current_year INT;
    DECLARE card_month INT;
    DECLARE card_year INT;

    -- Extract current month and year
    SET current_month = MONTH(CURDATE());
    SET current_year = YEAR(CURDATE());
    -- Extract month and year from the new credit card's expiration date
    SET card_month = SUBSTRING(NEW.expirationDate, 1, 2);
    SET card_year = SUBSTRING(NEW.expirationDate, 4, 2);

    -- Check if the expiration date is in the future
    IF (card_year < RIGHT(YEAR(NOW()), 2)) OR
       (card_year = RIGHT(YEAR(NOW()), 2) AND card_month < MONTH(NOW())) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Expiration date must be in the future';
    END IF;
END//

DELIMITER ;

DELIMITER //

-- Event to delete suspended accesses daily
CREATE EVENT deleteSuspendedAccess
ON SCHEDULE  EVERY 1 DAY STARTS CURDATE() DO
BEGIN
    -- Declare variables
    DECLARE accessId INT;
    DECLARE complete integer DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT access FROM suspendedAccess WHERE deletionDate <= CURDATE();
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET complete = TRUE;

    OPEN  cur;
    -- Loop through suspended accesses and delete them
    deleteAccesses :LOOP
        FETCH cur INTO accessId;
        -- Check if all accesses are processed
        IF (complete) THEN
            LEAVE deleteAccesses;
        END IF;

        -- Delete the access
        DELETE FROM access WHERE id = accessId;

    end loop deleteAccesses;
    -- Close cursor
    CLOSE cur;
END//

DELIMITER ;

