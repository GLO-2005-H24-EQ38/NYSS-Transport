DROP FUNCTION IF EXISTS SearchAccess;
DROP FUNCTION IF EXISTS RetrieveWallet;
DROP PROCEDURE IF EXISTS AddAccess;

DELETE FROM user where role = 'commuter' or role = 'admin';
DELETE FROM company where name = 'RTC Quebec';