use project;
DROP FUNCTION IF EXISTS SearchAccess;
DROP FUNCTION IF EXISTS RetrieveWallet;
DROP PROCEDURE IF EXISTS AddAccess;

-- TODO remove them eventually (takes down the sample data to check my methods)
# -- Rollback sample data from the transaction table
 DELETE FROM transaction WHERE accessId IN (1, 2);
#
# -- Rollback sample data from the subscription table
 DELETE FROM subscription WHERE access = 2;
#
# -- Rollback sample data from the ticket table
 DELETE FROM ticket WHERE access = 1;
#
# -- Rollback sample data from the admin table
 DELETE FROM admin WHERE user = 'admin@example.com';
#
# -- Rollback sample data from the commuter table
 DELETE FROM commuter WHERE user = 'user1@example.com';
#
# -- Rollback sample data from the access table
 DELETE FROM access WHERE id IN (1, 2, 3, 4, 5, 6);
#
# -- Rollback sample data from the company table
 DELETE FROM company WHERE name IN ('STM', 'RTC');
#
# -- Rollback sample data from the creditCard table
 DELETE FROM creditCard WHERE number IN (1234567890123456, 9876543210987654);
#
# -- Rollback sample data from the user table
 DELETE FROM user WHERE email IN ('user1@example.com', 'admin@example.com');
