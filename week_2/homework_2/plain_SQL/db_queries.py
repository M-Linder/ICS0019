import sqlite3

if __name__ == "__main__":
    # Connect to the database and start the transaction.
    conn = sqlite3.connect("plainDB")
    cursor = conn.cursor()

    # Specify the opening time and closing time to query between.
    open_time = "09:00"
    close_time = "16:20"

    # Query for canteens that fall in between the two provided times above.
    # Return the name of the canteens and their opening and closing hours.
    sql_command = """
    SELECT Name, time_open, time_closed FROM CANTEEN
    WHERE TIME(time_open) <= TIME(?)
    AND TIME(time_closed) >= TIME(?)"""

    cursor.execute(sql_command, (open_time, close_time))

    # Print the result as a list.
    print("RESTAURANTS OPEN FROM ")
    for row in cursor:
        print(row)

    # Specify the provider that will be queried in the following statement.
    provider_name = "Baltic Restaurants Estonia AS"

    # Query the locations which are provided by the provider specified above.
    # Return the name of the canteens and the provider's name.
    sql_command = """
    SELECT A.Name, B.ProviderName FROM CANTEEN A, PROVIDER B
    WHERE B.ProviderName == ?
    AND A.ProviderID == B.ID;
    """

    cursor.execute(sql_command, (provider_name,))

    # Print the result as a list.
    print("\n\n\nRESTAURANTS OPERATED BY BALTIC RESTAURANTS ESTONIA AS")
    for row in cursor:
        print(row)

    # Close the connection.
    conn.close()
