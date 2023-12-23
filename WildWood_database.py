import sqlite3

def add_person(Person_ID, First_Name, Last_Name, Residence, Ethnicity, Gender, Birthdate, Role):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        INSERT INTO Person(Person_ID, First_Name, Last_Name, Residence, Ethnicity, Gender, Birthdate, Role)
        VALUES(?,?,?,?,?,?,?,?);
        ''', (Person_ID, First_Name, Last_Name, Residence, Ethnicity, Gender, Birthdate, Role,))
    conn.commit()
    conn.close()
    
def del_person(Person_ID):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Person
        WHERE Person_ID = ?;
        ''', (Person_ID,))
    conn.commit()
    conn.close()

def add_complex(Complex_Number, Complex_Name, Complex_Location, Manager_ID):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        INSERT INTO Complex(Complex_Number, Complex_Name, Complex_Location, Manager_ID)
        VALUES(?,?,?,?);
        ''', (Complex_Number, Complex_Name, Complex_Location, Manager_ID,))
    conn.commit()
    conn.close()
    
def del_complex(Complex_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Complex
        WHERE Complex_Number = ?;
        ''', (Complex_Number,))
    conn.commit()
    conn.close()
    
def add_apartment(Apartment_Number, Apartment_Name, Apartment_Address, Complex_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foraign_keys = ON;')
    cur.execute('''
        INSERT INTO Apartment(Apartment_Number, Apartment_Name, Apartment_Address, Complex_Number)
        VALUES(?,?,?,?);
        ''', (Apartment_Number, Apartment_Name, Apartment_Address, Complex_Number,))
    conn.commit()
    conn.close()
    
def del_apartment(Apartment_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Apartment
        WHERE Apartment_Number = ?;
        ''', (Apartment_Number,))
    conn.commit()
    conn.close()
    
def add_lease(Lease_Number, Rent_Date, Rent_End, Rent_Amount, Deposit_Amount, Rent_Due, Tenant_ID, Late_Time, Late_Amount):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        INSERT INTO Lease_Information(Lease_Number, Rent_Date, Rent_End, Rent_Amount, Deposit_Amount, Rent_Due, Tenant_ID, Late_Time, Late_Amount)
        VALUES(?,?,?,?,?,?,?,?,?);
        ''', (Lease_Number, Rent_Date, Rent_End, Rent_Amount, Deposit_Amount, Rent_Due, Tenant_ID, Late_Time, Late_Amount,))
    conn.commit()
    conn.close()
    
def del_lease(Lease_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Lease_Information
        WHERE Lease_Number = ?;
        ''', (Lease_Number,))
    conn.commit()
    conn.close()
    
def add_maintenance_request(Request_ID, Request_Date, Request_Category, Description, Requester_ID, Apartment_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        INSERT INTO Maintenance_Request(Request_ID, Request_Date, Request_Category, Description, Requester_ID, Apartment_Number)
        VALUES(?,?,?,?,?,?);
        ''', (Request_ID, Request_Date, Request_Category, Description, Requester_ID, Apartment_Number,))
    conn.commit()
    conn.close()
    
def del_maintenance_request(Request_ID):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Maintenance_Request
        WHERE Request_ID = ?;
        ''', (Request_ID,))
    conn.commit()
    conn.close()
    
def add_maintenance_expense(Request_ID, Resolution_Date, Cost, Description, Insurance_Coverage):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    INSERT INTO Maintenance_Expense(Request_ID, Resolution_Date, Cost, Description, Insurance_Coverage)
    VALUES(?,?,?,?,?);
    ''', (Request_ID, Resolution_Date, Cost, Description, Insurance_Coverage,))
    conn.commit()
    conn.close()
    
def del_maintenance_expense(Request_ID):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Maintenance_Expense
        WHERE Request_ID = ?;
        ''', (Request_ID,))
    conn.commit()
    conn.close()
    
def add_per_apart(Person_ID, Apartment_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    INSERT INTO Person_Apartment(Person_ID, Apartment_Number)
    VALUES(?,?);
    ''', (Person_ID, Apartment_Number,))
    conn.commit()
    conn.close()
    
def del_per_apart(Person_ID, Apartment_Number):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
        DELETE FROM Person_Apartment
        WHERE Person_ID = ? AND Apartment_Number = ?;
        ''', (Person_ID, Apartment_Number,))
    conn.commit()
    conn.close()
    
def get_all_people():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Person;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_complex():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Complex;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_apartment():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Apartment;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_person_apartment():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Person_Apartment;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_lease():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Lease_Information;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_maintenance_request():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Maintenance_Request;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_all_maintenance_expense():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('SELECT * FROM Maintenance_Expense;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_lease_information(lease_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT * FROM Lease_Information
    WHERE Lease_Number = ?;
    ''', (lease_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_complex(complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT * FROM Complex
    WHERE Complex_Number = ?;
    ''', (complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_complex_address(complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT Complex_Location 
    FROM Complex
    WHERE Complex_Number = ?;
    ''', (complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_complex_count():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT COUNT(*) 
    FROM (
    SELECT Complex_Number FROM Complex);
    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_apartment_count(complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT COUNT(*) 
    FROM (
    SELECT Apartment_Number FROM Apartment
    WHERE Complex_Number = ?);
    ''', (complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_tenant_count(time1, time2, complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT COUNT(*)
    FROM (
    SELECT Lease_Number FROM Lease_Information
    WHERE Rent_Date <= ? AND Rent_End >= ? AND Tenant_ID IN (
        SELECT Person_ID FROM Person_Apartment
        WHERE Apartment_Number IN (
            SELECT Apartment_Number FROM Apartment
            WHERE Complex_Number = ?)));
    ''', (time1, time2, complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_revenue(time1, time2, complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT SUM(Rent_Amount) FROM Lease_Information
    WHERE Rent_Date >= ? AND Rent_Date <= ? AND Tenant_ID IN (
        SELECT Person_ID FROM Person_Apartment
        WHERE Apartment_Number IN (
            SELECT Apartment_Number FROM Apartment
            WHERE Complex_Number = ?));
    ''', (time1, time2, complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_year_revenue(year, complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT SUM(Rent_Amount) FROM Lease_Information
    WHERE strftime('%Y', Rent_Date) = ? AND Tenant_ID IN (
        SELECT Person_ID FROM Person_Apartment
        WHERE Apartment_Number IN (
            SELECT Apartment_Number FROM Apartment
            WHERE Complex_Number = ?));
    ''', (year, complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_expense(time1, time2, complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT L.Request_Category, R.Cost, R.Insurance_Coverage
    FROM
        Maintenance_Request AS L
        INNER JOIN Maintenance_Expense AS R ON L.Request_ID = R.Request_ID
        WHERE R.Resolution_Date >= ? AND R.Resolution_Date <= ? AND L.Apartment_Number IN (
            SELECT Apartment_Number FROM Apartment
            WHERE Complex_Number = ?)
    GROUP BY L.Request_Category;
    ''', (time1, time2, complex_num))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_changing_tenant(time1, time2, complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT COUNT(*)
    FROM (
        SELECT L.Tenant_ID
        FROM 
            Lease_Information AS L
            INNER JOIN Lease_Information AS R ON L.Rent_Date >= R.Rent_End
            INNER JOIN Person_Apartment AS M1 ON L.Tenant_ID = M1.Person_ID
            INNER JOIN Person_Apartment AS M2 ON R.Tenant_ID = M2.Person_ID
            WHERE (R.Rent_End >= ? AND L.Rent_Date <= ? AND L.Rent_Date >= R.Rent_End) AND L.Tenant_ID <> R.Tenant_ID AND M1.Apartment_Number = M2.Apartment_Number AND M1.Apartment_Number IN (
                SELECT Apartment_Number FROM Apartment
                WHERE Complex_Number = ?));
    ''', (time1, time2, complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_complex_num():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT Complex_Number FROM Complex;
    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_tenant_id():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT Person_ID FROM Person
    WHERE Role = 'Tenant';
    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_lease_number():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT Lease_Number FROM Lease_Information;
    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_tenant_infor(tenant_id):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT * FROM Person
    WHERE Person_ID = ?;
    ''', (tenant_id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_num_lease(tenant_id):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT Lease_Number FROM Lease_Information
    WHERE Tenant_ID = ?;
    ''', (tenant_id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_lease_t(lease_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT * FROM Lease_Information
    WHERE Lease_Number = ?;
    ''', (lease_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_complex_total_revenue(complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT SUM(Rent_Amount) FROM Lease_Information
    WHERE Tenant_ID IN (
        SELECT Person_ID FROM Person_Apartment
        WHERE Apartment_Number IN (
            SELECT Apartment_Number FROM Apartment
            WHERE Complex_Number = ?));
    ''', (complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_complex_total_expense(complex_num):
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT L.Request_Category, R.Cost, R.Insurance_Coverage
    FROM
        Maintenance_Request AS L
        INNER JOIN Maintenance_Expense AS R ON L.Request_ID = R.Request_ID
        WHERE L.Apartment_Number IN (
            SELECT Apartment_Number FROM Apartment
            WHERE Complex_Number = ?)
    GROUP BY L.Request_Category;
    ''', (complex_num,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_total_revenue():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT SUM(Rent_Amount) FROM Lease_Information;
    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_total_expense():
    conn = sqlite3.connect('WildWood.db')
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''
    SELECT L.Request_Category, R.Cost, R.Insurance_Coverage
    FROM
        Maintenance_Request AS L
        INNER JOIN Maintenance_Expense AS R ON L.Request_ID = R.Request_ID
    GROUP BY L.Request_Category;
    ''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows