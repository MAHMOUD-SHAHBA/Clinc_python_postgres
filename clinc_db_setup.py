import psycopg
from psycopg import sql

#-------   Database Connection ---------------------
DB_HOST = "localhost"
DB_NAME = "clinic_db"
DB_USER = "postgres"
DB_PASSWORD = ""
DB_PORT = "5432"


CLINIC_DB = "clinic_db"

try:
    conn = psycopg.connect(
        host = DB_HOST ,
        dbname = DB_NAME ,
        user = DB_USER,
        password= DB_PASSWORD ,
        port = DB_PORT
    )
    conn.autocommit = True
    cr = conn.cursor()
    cr.execute(sql.SQL(
        "CREATE DATABASE {}".format(sql.Identifier(CLINIC_DB))
    ))
    print(f"Database '{CLINIC_DB}' created successfully.")
except psycopg.errors.DuplicateDatabase:
    print(f"Database '{CLINIC_DB}' already exists.")
except Exception as e :
    print(f" Error" , e)
finally:
    if conn :
        cr.close()
        conn.close()

#------- connect to the new created database Clinic_db ---------
try:
    conn = psycopg.connect(
        host = DB_HOST ,
        dbname = DB_NAME ,
        user = DB_USER,
        password= DB_PASSWORD ,
        port = DB_PORT
    )
    conn.autocommit = True
    cr = conn.cursor()
    print(f"Connected to database '{CLINIC_DB}'")

except Exception as e :
    print("Error" , e )
    exit()

#-------         Create  Tables  -------------------------
#------- Patients Table --------
cr.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id SERIAL PRIMARY KEY ,
        fisrt_name VARCHAR(50) NOT NULL  ,
        last_name VARCHAR(50) NOT NULL ,
        dob DATE ,
        gender VARCHAR(10),
        phone VARCHAR(20),
        email VARCHAR(100),
        address TEXT , 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
""")


#------- Staff Table ------------------------

cr.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        staff_id SERIAL PRIMARY KEY ,
        first_name VARCHAR(50) NOT NULL ,
        last_name VARCHAR(50) NOT NULL ,
        role VARCHAR(50) NOT NULL , -- Doctor , Nurse , Receptionist , Admin
        phone VARCHAR(20),
        email vARCHAR(100),
        username VARCHAR(50) UNIQUE ,
        password VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
""")


#-------   Appointments -----------------
cr.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id SERIAL PRIMARY KEY ,
        patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
        doctor_id INT NOT NULL REFERENCES staff(staff_id) ON DELETE CASCADE ,
        appointment_date DATE NOT NULL,
        appointment_time TIME NOT NULL ,
        status VARCHAR(20) DEFAULT 'Scheduled', -- Scheduled , Completed ,Cancelled
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
""")

#------- Billing Table  --------------------------
cr.execute("""
    CREATE TABLE IF NOT EXISTS billig(
        bill_id SERIAL pRIMARY KEY ,
        appointment_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE ,
        amount DECIMAL(10,2) NOT NULL ,
        payment_status VARCHAR(50) DEFAULT 'Pending', -- Paid , Pending
        payment_method VARCHAR(50), -- Cash , Card , Insurance
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
""")

#-------  Lab Reports Table ------------------
cr.execute("""
    CREATE TABLE IF NOT EXISTS lab_reports(
        report_id SERIAL PRIMARY KEY,
        patient_id INT NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
        doctor_id INT REFERENCES staff(staff_id),
        test_name VARCHAR(100) NOT NULL,
        test_date DATE NOT NULL ,
        result TEXT,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
""")

#-------    Settings Table ------------------------------
cr.execute("""
    CREATE TABLE IF NOT EXISTS settings(
        setting_id SERIAL PRIMARY KEY ,
        clinic_name VARCHAR(100) Default 'Heilpraxis',
        address TEXT ,
        phone VARCHAR(20),
        email VARCHAR(100),
        working_hours VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );
""")

print("All tables created successfully.")

#-------      Close Connection -----------
cr.close()
conn.close()
print("Database connection closed")