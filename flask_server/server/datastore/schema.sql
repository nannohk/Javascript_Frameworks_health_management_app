DROP TABLE IF EXISTS "insurance";
DROP TABLE IF EXISTS "patient";
DROP TABLE IF EXISTS "user";

CREATE TABLE "user"(
    email Varchar2(100) PRIMARY KEY,
    password Varchar2(100),
    fullName varchar2(200),
    role varchar2(100),
    profileImage blob,
    address varchar2(200),
    gender varchar2(10),
    license boolean
);

CREATE TABLE "patient"(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender varchar2(10),
    fullName varchar2(200),
    address varchar2(200),
    patientImage blob,
    phoneNumber varchar2(20),
    employer varchar2(200),
    employerAddress varchar2(200),
    position varchar2(200),
    dateOfBirth date,
    caregiverEmail varchar2(100),
    caregiverName varchar2(200),
    foreign key (caregiverEmail) references user(email),
     foreign key (caregiverName) references user(fullName)
);

CREATE TABLE "insurance"(
    id INTEGER PRIMARY KEY,
    insuranceCompany varchar2(200),
    policyNumber varchar2(200),
    groupNumber varchar2(20),
    insuredParty varchar2(100),
    relationship varchar2(100),
    patientId INTEGER,
        foreign key (patientId) references patient(id)
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