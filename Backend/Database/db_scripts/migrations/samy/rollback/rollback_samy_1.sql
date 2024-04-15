
DELETE FROM user WHERE email = 'whatever@what.com';
DELETE FROM user WHERE email = 'yo@yo.com';
DELETE FROM user WHERE email = 'Rando@rand.ran';
DELETE FROM user WHERE email = 'hello@whatsup.hi';
DELETE FROM user WHERE email = 'yolo@theRealones.real';
DELETE FROM user WHERE email = 'Nocredit@nobitches.L';

DELETE FROM creditcard WHERE number = '12345';
DELETE FROM creditcard WHERE number = '1234567890';
DELETE FROM creditcard WHERE number = '123123456789';


DROP PROCEDURE IF EXISTS addCreditcard;
DROP PROCEDURE IF EXISTS replaceCreditcard;
