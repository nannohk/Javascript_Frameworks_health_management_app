DROP TABLE IF EXISTS "users";

CREATE TABLE "users"(
    email Varchar2(100) PRIMARY KEY,
    password Varchar2(100),
    fullname varchar2(200),
    role varchar2(100),
    profileImage blob,
    address varchar2(200),
    gender varchar2(10),
    license boolean
);

-- CREATE view admin_list as
-- select
--     email,
--     fullname,
--     role,
--     gender,
--     address,
--     license
-- from
--     users;