DROP FUNCTION IF EXISTS RetrieveWallet;
DROP FUNCTION IF EXISTS AddAccess;



DELIMITER //
-- Function to add an access
CREATE FUNCTION AddAccess(
    p_access_id VARCHAR(100),
    p_access_name VARCHAR(1000),
    p_price FLOAT,
    p_company_name VARCHAR(100),
    p_access_type enum('ticket','subscription'),
    p_duration INT,
    p_numberOfPassage integer
) RETURNS VARCHAR(10000) DETERMINISTIC
BEGIN
    -- Declare variable for access info
    DECLARE access_created VARCHAR(10000);

    -- Insert the company if it does not exist
    INSERT IGNORE INTO company (name) VALUES (p_company_name);

    -- Insertion into the table access
    INSERT INTO access (id, name, price, company, type, duration)
    VALUES (p_access_id, p_access_name, p_price, p_company_name, p_access_type, p_duration);

    -- Insertion into the appropriate table based on the access type
    IF p_access_type = 'ticket' THEN
        INSERT INTO ticket (access, passes) VALUES (p_access_id, p_numberOfPassage);
    ELSEIF p_access_type = 'subscription' THEN
        INSERT INTO subscription (access) VALUES (p_access_id);
    END IF;

    -- Set the JSON array for an added access
    SET access_created = CONCAT(
    '{"accessId": "', p_access_id, '",',
    '"accessName": "', p_access_name, '",',
    '"price": "', p_price, '",',
    '"accessType": "', p_access_type, '",',
    '"duration": "', p_duration, '",',
    '"company": "', p_company_name, '"',
    IF(p_access_type = 'ticket', CONCAT(',"numberOfPassage": "', p_numberOfPassage, '"'), ''),
    '}'
);

    RETURN access_created;
END //
DELIMITER ;

