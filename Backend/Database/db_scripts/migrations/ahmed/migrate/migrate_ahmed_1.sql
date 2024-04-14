DROP FUNCTION IF EXISTS CompanyExists;
DROP PROCEDURE IF EXISTS RegisterCommuter;
DROP PROCEDURE IF EXISTS RegisterAdmin;
DROP PROCEDURE IF EXISTS LoginUser;

DELIMITER //

-- Function to check if a company exists
CREATE FUNCTION CompanyExists(p_company VARCHAR(100)) RETURNS INT DETERMINISTIC
BEGIN
    -- Declare variable to hold the count of companies with the given name
    DECLARE company_count INT;
    -- Count the number of companies with the given name
    SELECT COUNT(*) INTO company_count FROM company u WHERE u.name = p_company;
    RETURN company_count;
END //

-- Procedure to register a commuter
CREATE PROCEDURE RegisterCommuter(
    IN p_email VARCHAR(100),
    IN p_name VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_address VARCHAR(50),
    IN p_dob DATE,
    IN p_phone BIGINT
)
BEGIN
-- Insert user information into the user table
INSERT INTO user (email, name, password, address, birthday, phone, role)
VALUES (p_email, p_name, p_password, p_address, p_dob, p_phone, 'commuter');
-- Insert commuter information into the commuter table
INSERT INTO commuter (user)
VALUES (p_email);
END //

-- Procedure to register an admin
CREATE PROCEDURE RegisterAdmin(
    IN p_email VARCHAR(100),
    IN p_name VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_address VARCHAR(50),
    IN p_dob DATE,
    IN p_phone BIGINT,
    IN p_admin_code VARCHAR(100),
    IN p_company VARCHAR(100)
)
BEGIN
    -- Check if the company exists, if not, insert it
    IF (SELECT CompanyExists(p_company)) = 0 THEN
        INSERT INTO company (name)
            VALUES (p_company);
        END IF;
    -- Insert user information into the user table
    INSERT INTO user (email, name, password, address, birthday, phone, role)
    VALUES (p_email, p_name, p_password, p_address, p_dob, p_phone, 'admin');
    -- Insert admin information into the admin table
    INSERT INTO admin (user, code, company)
    VALUES (p_email, p_admin_code, p_company);
END //

-- Procedure to login a user
CREATE PROCEDURE LoginUser(
    IN p_email VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_admin_code VARCHAR(100)
)
BEGIN
    -- Declare variable to hold the role of the user
    DECLARE user_role ENUM('commuter', 'admin');
    -- Retrieve the role of the user based on email and password
    SELECT role INTO user_role FROM user
    WHERE email = p_email AND password = p_password;

    -- If user role is not found, signal an error
    IF user_role IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email or password';
    ELSE
        -- Check user role and perform actions accordingly
        CASE user_role
            WHEN 'commuter' THEN
                -- If user is a commuter, select commuter information
                SELECT * FROM commuter WHERE user = p_email;
            WHEN 'admin' THEN
                -- If user is an admin, check if admin code is provided
                IF p_admin_code IS NULL THEN
                    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Admin code is required for admin login';
                ELSE
                    -- Select admin information if admin code is provided
                    SELECT * FROM admin WHERE user = p_email AND code = p_admin_code;
                END IF;
        END CASE;
    END IF;
END; //
DELIMITER ;

-- TODO remove this once data added
CALL RegisterCommuter('Samy@sa.my', 'Samy','sami:)','Quebec', '2000-01-01', 4521445987);
CALL RegisterCommuter('Nasma@nas.ma', 'Nasma','nasooma','Quebec', '2000-01-01', 4521445987);
CALL RegisterCommuter('Yannick@yann.ick', 'Yannick','the_one_true_yannick','Quebec', '2000-01-01', 4521445987);
CALL RegisterAdmin('admin@nyss.ca', 'Incognito', 'fishing_with_an_f', 'Montreal', '1900-01-01', '4185559999', 52, 'RTC Quebec');