DROP FUNCTION IF EXISTS EmailExists;
DROP PROCEDURE IF EXISTS RegisterUser;
DROP PROCEDURE IF EXISTS LoginUser;

DELIMITER //
# CREATE FUNCTION EmailExists(p_email VARCHAR(100)) RETURNS INT DETERMINISTIC
# BEGIN
#     DECLARE email_count INT;
#     SELECT COUNT(*) INTO email_count FROM user u WHERE u.email = p_email;
#     RETURN email_count;
# END //

CREATE PROCEDURE RegisterUser(
    IN p_email VARCHAR(100),
    IN p_name VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_address VARCHAR(50),
    IN p_dob DATE,
    IN p_phone BIGINT,
    IN p_role enum('commuter', 'admin'),
    IN p_admin_code integer,
    IN p_company VARCHAR(100)
)
BEGIN
#     DECLARE email_exists INT;
#
#     -- Check if the email already exists
#     SET email_exists = EmailExists(p_email);
#
#     -- If email exists, do not proceed with registration
#     IF email_exists > 0 THEN
#         SIGNAL SQLSTATE '45000'
#             SET MESSAGE_TEXT = 'Email already exists';
#     ELSE
    INSERT INTO user (email, name, password, address, birthday, phone, role)
    VALUES (p_email, p_name, p_password, p_address, p_dob, p_phone, p_role);

    IF p_role = 'commuter' THEN
    INSERT INTO commuter (user)
    VALUES (p_email);
    ELSEIF p_role = 'admin' and p_admin_code != 0 THEN
    INSERT INTO admin (user, code)
    VALUES (p_email, p_admin_code);
    END IF;
END //

CREATE PROCEDURE LoginUser(
    IN p_email VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_admin_code integer
)
BEGIN
    DECLARE user_role ENUM('commuter', 'admin');

    SELECT role INTO user_role FROM user
    WHERE email = p_email AND password = p_password;

    IF user_role IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email or password';
    ELSE
        CASE user_role
            WHEN 'commuter' THEN
                SELECT * FROM commuter WHERE user = p_email;
            WHEN 'admin' THEN
                IF p_admin_code IS NULL THEN
                    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Admin code is required for admin login';
                ELSE
                    SELECT * FROM admin WHERE user = p_email AND code = p_admin_code;
                END IF;
        END CASE;
    END IF;
END; //
DELIMITER ;

CALL RegisterUser('Samy@sa.my', 'Samy','sami:)','Quebec', '2000-01-01', 4521445987,'commuter' ,0, NULL);
CALL RegisterUser('Nasma@nas.ma', 'Nasma','nasooma','Quebec', '2000-01-01', 4521445987,'commuter' ,0, NULL);
CALL RegisterUser('Yannick@yann.ick', 'Yannick','the_one_true_yannick','Quebec', '2000-01-01', 4521445987,'commuter' ,0, NULL);
CALL RegisterUser('admin1@nyss.ca', 'Incognito', 'fishing_with_an_f', 'Montreal', '1900-01-01', '4185559999', 'admin', 5, 'RTC Quebec');
