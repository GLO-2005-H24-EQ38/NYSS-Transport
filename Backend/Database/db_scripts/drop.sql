/* procedures to drop if not dropped */
DROP PROCEDURE IF EXISTS addCreditcard;

/* Drop first due to FOREIGN KEY Constraints */
Drop TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS commuter;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS subscription;


/*No FOREIGN KEY constraints */
DROP TABLE  IF EXISTS user CASCADE;
DROP TABLE IF EXISTS access;
DROP TABLE IF EXISTS creditCard;
DROP TABLE IF EXISTS company;