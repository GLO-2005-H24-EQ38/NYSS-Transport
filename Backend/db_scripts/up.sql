CREATE TABLE user (
    email varchar(100),
    name varchar(100) NOT NULL ,
    password varchar(100) NOT NULL ,
    address varchar(100) NOT NULL ,
    birthday date NOT NULL ,
    phone varchar(20),
    role enum('commuter','admin') DEFAULT 'commuter' NOT NULL ,
    PRIMARY KEY (email)
);

CREATE TABLE creditCard (
    number integer,
    holderName varchar(100) NOT NULL ,
    expirationDate char(5) NOT NULL ,
    PRIMARY KEY (number)
);

CREATE TABLE company (
    name varchar(100),
    PRIMARY KEY (name)
);

CREATE TABLE access (
    number integer,
    name varchar(100) NOT NULL ,
    price float NOT NULL ,
    company varchar(100),
    type enum('ticket','subscription') NOT NULL,
    expiration date NOT NULL,
    PRIMARY KEY (Number),
    FOREIGN KEY (company) REFERENCES company (name) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE commuter(
    user varchar(100),
    creditCard INTEGER(10) ,
    PRIMARY KEY (user),
    FOREIGN KEY (user) REFERENCES user (email) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (creditCard) references creditCard(number) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE admin(
    user varchar(100),
    code integer NOT NULL ,
    company varchar(100),
    PRIMARY KEY (user),
    FOREIGN KEY (user) REFERENCES user (email) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (company) REFERENCES company (name) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE ticket(
    access integer,
    passes integer NOT NULL,
    PRIMARY KEY (access),
    FOREIGN KEY (access) REFERENCES access (Number) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE subscription (
    access integer,
    start DATE,
    PRIMARY KEY (access),
    FOREIGN KEY (access) REFERENCES access (Number) ON UPDATE CASCADE ON DELETE CASCADE
);

