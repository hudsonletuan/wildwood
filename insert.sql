PRAGMA foreign_keys = ON;
INSERT INTO Person
VALUES
    ('M101', 'Zinedine', 'Zidane', 'France', 'Ethnic1', 'Male', '1972-06-23', 'Headquarter Manager'),
    ('M102', 'Jurgen', 'Klopp', 'Germany', 'Ethnic2', 'Male', '1967-06-16', 'Headquarter Manager'),
    ('M103', 'Becky', 'Burleigh', 'United States', 'Ethnic3', 'Female', '1967-10-13', 'Headquarter Manager'),
    ('M201', 'Harry', 'Maguire', 'Washington', 'Ethnic1', 'Male', '1993-03-05', 'Complex Manager'),
    ('M202', 'Cristiano', 'Ronaldo', 'Oregon', 'Ethnic2', 'Male', '1985-02-05', 'Complex Manager'),
    ('M203', 'Lionel', 'Messi', 'California', 'Ethnic3', 'Male', '1987-06-24', 'Complex Manager'),
    ('M204', 'Erica', 'Dambach', 'Idaho', 'Ethnic2', 'Female', '1975-11-16', 'Complex Manager'),
    ('T001', 'Charles', 'Summers', 'Chicago', 'Ethnic1', 'Male', '1982-02-13', 'Tenant'),
    ('T002', 'Marilyn', 'Newton', 'Texas', 'Ethnic2', 'Female', '1977-06-01', 'Tenant'),
    ('T003', 'Janice', 'Lewis', 'Iowa', 'Ethnic1', 'Female', '1992-12-23', 'Tenant'),
    ('T004', 'Larry', 'Thomas', 'Las Vegas', 'Ethnic3', 'Male', '1979-11-01', 'Tenant'),
    ('T005', 'Mark', 'Patterson', 'Washington DC', 'Ethnic1', 'Male', '1997-09-12', 'Tenant'),
    ('T006', 'Martin', 'Scheller', 'Idaho', 'Ethnic2', 'Male', '1961-10-31', 'Tenant'),
    ('T007', 'Roberta', 'Louise', 'Texas', 'Ethnic2', 'Female', '1995-11-23', 'Tenant'),
    ('T008', 'Sue', 'Tam', 'California', 'Ethnic3', 'Female', '1988-06-30', 'Tenant'),
    ('T009', 'Laura', 'Henderson', 'Iowa', 'Ethnic3', 'Female', '1990-02-28', 'Tenant'),
    ('T010', 'Thomas', 'Jones', 'Florida', 'Ethnic1', 'Male', '1977-10-01', 'Tenant'),
    ('T011', 'Shannon', 'Hall', 'Chicago', 'Ethnic1', 'Female', '1962-12-12', 'Tenant'),
    ('T012', 'Bob', 'Newton', 'Chicago', 'Ethnic3', 'Male', '1986-03-21', 'Tenant'),
    ('T013', 'Dennis', 'Smith', 'Iowa', 'Ethnic3', 'Male', '1998-01-01', 'Tenant');

INSERT INTO Complex(Complex_Number, Complex_Name, Complex_Location, Manager_ID)
VALUES (1, "Idaho Wildwood Apartment Complex", "Caldwell,ID", "M201"),
       (2, "Idaho Wildwood Apartment Complex", "Boise,ID", "M202"),
       (3, "California Wildwood Apartment Complex", "San Diago,CA", "M203"),
       (4, "Oregan Wildwood Apartment Complex", "Portland,OR", "M204");

INSERT INTO Apartment(Apartment_Number, Apartment_Name, Apartment_Address, Complex_Number)
VALUES (101, "Apartment A", "2110 Cleveland Blvd", 1),
       (102, "Apartment B", "2110 Cleveland Blvd", 1),
       (103, "Apartment A", "1115 N Milwakee st.", 1),
       (110, "Apartment A", "1115 N Milwakee st.", 1),
       (113, "Apartment A", "1115 N Milwakee st.", 1),
       (201, "Apartment A", "5320 Chicago St.", 2),
       (207, "Apartment A", "5320 Chicago St.", 2),
       (209, "Apartment A", "2110 Acharya Blvd", 3),
       (303, "Apartment A", "2110 Acharya Blvd", 3),
       (306, "Apartment A", "2110 Acharya Blvd", 3),
       (311, "Apartment A", "2110 Acharya Blvd", 3);
       
INSERT INTO Person_Apartment(Person_ID, Apartment_Number)
VALUES --("M201", 156),
       --("M202", 299),
       --("M203", 333),
       --("M204", 459),
       ("T001", 201),
       --("T002", 110),
       --("T003", 306),
       ("T004", 110),
       ("T005", 306),
       --('T006', 203),
       ('T007', 311),
       --('T008', 111),
       ('T009', 207),
       --('T010', 110),
       ('T011', 311),
       ('T012', 102),
       ('T013', 209);

INSERT INTO Lease_Information (Lease_Number, Rent_Date, Rent_End, Rent_Amount, Deposit_Amount, Rent_Due, Tenant_ID, Late_Time, Late_Amount)
VALUES (201050109, '2013-05-01', '2014-05-01', 1500, 3500, "15th", "T001", "0 days", 0),
       (110060109, '2013-06-01', '2013-12-01', 1200, 2900, "13th", "T004", "5 Days", 50),
       (306060109, '2013-06-01', '2014-06-01', 1250, 3000, "12th", "T005", "10 Days", 100),
       (102060109, '2013-06-01', '2014-06-01', 1250, 3000, "1st", "T012", "0 Days", 0),
       (209060109, '2013-04-09', '2013-12-01', 1450, 3400, "2nd", "T013", "0 Days", 0),
       (204556668, '2013-01-01', '2013-06-01', 1450, 3400, "2nd", "T007", "0 Days", 0),
       (204590668, '2013-06-08', '2014-02-01', 1450, 3400, "2nd", "T011", "0 Days", 0),
       (209034109, '2014-02-01', '2014-06-01', 1450, 3400, "2nd", "T013", "5 Days", 50),
       (209758949, '2014-07-15', '2014-12-01', 1450, 3400, "2nd", "T013", "5 Days", 50);
       
INSERT INTO Maintenance_Request
VALUES
    ('R001', '2013-05-05', 'electrical', 'Left burner out on range', 'M203', 303),
    ('R002', '2013-05-05', 'floor', 'Water wastage from overflowing bathtub', 'T001', 209),
    ('R003', '2013-05-06', 'plumbing', 'Dishwasher backing up', 'M201', 311),
    ('R004', '2013-05-15', 'walls', 'Hole in plaster', 'T009', 209),
    ('R005', '2013-05-15', 'utilities', 'Refrigerator failed', 'M201', 306);

INSERT INTO Maintenance_Expense (Request_ID, Resolution_Date, Cost, Description, Insurance_Coverage)
VALUES ('R001', '2013-06-10', 150,"Electrician rewired", 50),
       ('R002', '2013-06-21', 550, "Replaced flooring new tile", 30),
       ('R003', '2013-06-06', 35, "Filter clogged; cleared it", 100),
       ('R004', '2013-06-17', 250, "Patched hole", 0),
       ('R005', '2013-06-20', 690, "New refrigerator", 100);