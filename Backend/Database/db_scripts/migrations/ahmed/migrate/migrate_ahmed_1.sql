DROP FUNCTION IF EXISTS EmailExists;
DROP PROCEDURE IF EXISTS RegisterCommuter;
DROP PROCEDURE IF EXISTS RegisterAdmin;
DROP PROCEDURE IF EXISTS LoginUser;

DELIMITER //
CREATE PROCEDURE RegisterCommuter(
    IN p_email VARCHAR(100),
    IN p_name VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_address VARCHAR(50),
    IN p_dob DATE,
    IN p_phone BIGINT
)
BEGIN
INSERT INTO user (email, name, password, address, birthday, phone, role)
VALUES (p_email, p_name, p_password, p_address, p_dob, p_phone, 'commuter');
INSERT INTO commuter (user)
VALUES (p_email);
END //

CREATE PROCEDURE RegisterAdmin(
    IN p_email VARCHAR(100),
    IN p_name VARCHAR(100),
    IN p_password VARCHAR(100),
    IN p_address VARCHAR(50),
    IN p_dob DATE,
    IN p_phone BIGINT,
    IN p_admin_code integer,
    IN p_company VARCHAR(100)
)
BEGIN
INSERT INTO company (name)
VALUES (p_company);
INSERT INTO user (email, name, password, address, birthday, phone, role)
VALUES (p_email, p_name, p_password, p_address, p_dob, p_phone, 'admin');
INSERT INTO admin (user, code, company)
VALUES (p_email, p_admin_code, p_company);
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
CALL RegisterCommuter('Samy@sa.my', 'Samy','sami:)','Quebec', '2000-01-01', 4521445987);
CALL RegisterCommuter('Nasma@nas.ma', 'Nasma','nasooma','Quebec', '2000-01-01', 4521445987);
CALL RegisterCommuter('Yannick@yann.ick', 'Yannick','the_one_true_yannick','Quebec', '2000-01-01', 4521445987);
CALL RegisterAdmin('admin@nyss.ca', 'Incognito', 'fishing_with_an_f', 'Montreal', '1900-01-01', '4185559999', 52, 'RTC Quebec');