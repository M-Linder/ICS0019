import sqlite3

if __name__ == "__main__":
    # Create the DB if it doesn't exist and start the transaction.
    conn = sqlite3.connect("plainDB")
    cursor = conn.cursor()

    # Drop Provider and Canteen tables if they exist for a fresh start.
    sql_command = """
            DROP table IF EXISTS PROVIDER;"""

    cursor.execute(sql_command)

    sql_command = """
        DROP table IF EXISTS CANTEEN;"""

    cursor.execute(sql_command)

    # Create the provider table.
    sql_command = """
        CREATE TABLE PROVIDER (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProviderName TEXT
        );"""

    cursor.execute(sql_command)

    # Create the canteen table.
    sql_command = """
    CREATE table CANTEEN (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProviderID INTEGER,
        Name TEXT,
        Location TEXT,
        time_open TEXT,
        time_closed TEXT,
        FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ID)
    );"""

    cursor.execute(sql_command)

    # Insert canteen providers into provider table.
    sql_command = """
        INSERT INTO PROVIDER (ProviderName)
        VALUES
            ('Rahva Toit'),
            ('Baltic Restaurants Estonia AS'),
            ('TTÜ Sport OÜ')
        ;"""

    cursor.execute(sql_command)

    # Insert canteens into canteen table.
    sql_command = """
        INSERT INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed)
        VALUES
            (1, 'Economics- and social science building canteen', 'Akadeemia tee 3, SOC- building', '08:30', '18:30'),
            (1, 'Library canteen', 'Akadeemia tee 1/Ehitajate tee 7', '08:30', '19:00'),
            (2, 'Main building Deli cafe', 'Ehitajate tee 5, U01 building', '09:00', '16:30'),
            (2, 'Main building Daily lunch restaurant', 'Ehitajate tee 5, U01 building', '09:00', '16:30'),
            (1, 'U06 building canteen', 'Ehitajate tee 5, U06 building', '09:00', '16:00'),
            (2, 'Natural Science building canteen', 'Akadeemia tee 15, SCI building', '09:00', '16:00'),
            (2, 'ICT building canteen', 'Raja 15/Mäepealse 1', '09:00', '16:00'),
            (3, 'Sports building canteen', 'Männiliiva 7, S01 building', '11:00', '20:00')
        ;"""

    cursor.execute(sql_command)

    # Insert ITCollege provider and canteen separately into the tables.
    sql_command = """
        INSERT INTO PROVIDER (ProviderName)
        VALUES ('Bitt OÜ');"""

    cursor.execute(sql_command)

    sql_command = """
        INSERT INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed)
        VALUES (4, 'bitStop KOHVIK', 'IT College, Raja 4c', '09:30', '16:00');"""

    cursor.execute(sql_command)

    # Commit changes to the database and close the connection.
    conn.commit()
    conn.close()
