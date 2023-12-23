DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Complex;
DROP TABLE IF EXISTS Apartment;
DROP TABLE IF EXISTS Person_Apartment;
DROP TABLE IF EXISTS Lease_Information;
DROP TABLE IF EXISTS Maintenance_Request;
DROP TABLE IF EXISTS Maintenance_Expense;

CREATE TABLE Person(
    Person_ID TEXT NOT NULL PRIMARY KEY,
    First_Name TEXT,
    Last_Name TEXT,
    Residence TEXT,
    Ethnicity TEXT,
    Gender TEXT,
    Birthdate TEXT,
    Role TEXT
);

CREATE TABLE Complex(
    Complex_Number INTEGER NOT NULL PRIMARY KEY,
    Complex_Name TEXT,
    Complex_Location TEXT,
    Manager_ID TEXT,
    FOREIGN KEY(Manager_ID) REFERENCES Person(Person_ID)
);

CREATE TABLE Apartment(
    Apartment_Number INTEGER NOT NULL PRIMARY KEY,
    Apartment_Name TEXT,
    Apartment_Address TEXT,
    Complex_Number INTEGER,
    FOREIGN KEY(Complex_Number) REFERENCES Complex(Complex_Number)
);

CREATE TABLE Person_Apartment(
    Person_ID TEXT NOT NULL PRIMARY KEY,
    Apartment_Number INTEGER,
    FOREIGN KEY(Person_ID) REFERENCES Person(Person_ID),
    FOREIGN KEY(Apartment_Number) REFERENCES Apartment(Apartment_Number)
);

CREATE TABLE Lease_Information (
    Lease_Number INTEGER NOT NULL,
    Rent_Date TEXT,
    Rent_End TEXT,
    Rent_Amount REAL,
    Deposit_Amount REAL,
    Rent_Due REAL,
    Tenant_ID TEXT,
    Late_Time TEXT,
    Late_Amount REAL,
    PRIMARY KEY (Lease_Number)
    FOREIGN KEY(Tenant_ID) REFERENCES Person_Apartment(Person_ID)
);

CREATE TABLE Maintenance_Request (
    Request_ID TEXT NOT NULL,
    Request_Date TEXT,
    Request_Category TEXT,
    Description TEXT,
    Requester_ID TEXT,
    Apartment_Number INTEGER,
    PRIMARY KEY (Request_ID),
    FOREIGN KEY (Apartment_Number) REFERENCES Apartment(Apartment_Number)
    FOREIGN KEY (Requester_ID) REFERENCES Person(Person_ID)
);

CREATE TABLE Maintenance_Expense (
    Request_ID TEXT NOT NULL,
    Resolution_Date TEXT,
    Cost REAL,
    Description TEXT,
    Insurance_Coverage REAL,
    PRIMARY KEY (Request_ID),
    FOREIGN KEY (Request_ID) REFERENCES Maintenance_Request(Request_ID)
);

