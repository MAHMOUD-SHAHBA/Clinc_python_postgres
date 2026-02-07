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
