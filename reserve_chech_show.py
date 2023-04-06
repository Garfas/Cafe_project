import sqlite3
from datetime import datetime

def connect_to_database():
    conn = sqlite3.connect('Table_reservations.db')
    c = conn.cursor()
    return conn, c

def create_reservations_table():
    conn, c = connect_to_database()
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    table_number INTEGER NOT NULL,
                    reservation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def make_reservation():
    conn, c = connect_to_database()
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    table_number = input("Enter the table number: ")
    reservation_date_str = input("Enter the reservation date and time (YYYY-MM-DD HH:MM:SS): ")
    reservation_date = datetime.strptime(reservation_date_str, "%Y-%m-%d %H:%M:%S")
    c.execute('''INSERT INTO reservations (name, surname, phone_number, table_number, reservation_date)
                    VALUES (?, ?, ?, ?, ?)''', (name, surname, phone_number, table_number, reservation_date))
    conn.commit()
    conn.close()
    print("Reservation successful!")

def check_reservation():
    conn, c = connect_to_database()
    name = input("Enter name to check reservation information: ")
    surname = input("Enter surname to check reservation information: ")
    c.execute("SELECT table_number FROM reservations WHERE name=? AND surname=?", (name, surname))
    result = c.fetchone()
    if result is not None:
        print(f"{name} {surname} has reserved table number {result[0]}.")
    else:
        print(f"No reservation found for {name} {surname}.")
    conn.close()

def show_all_reservations():
    conn, c = connect_to_database()
    c.execute("SELECT * FROM reservations")
    result = c.fetchall()
    if result:
        print("All reservations:")
        for row in result:
            print(f"Reservation ID: {row[0]}")
            print(f"name: {row[1]} {row[2]}")
            print(f"Phone Number: {row[3]}")
            print(f"Table number: {row[4]}")    
            print(f"Reservation Date: {row[5]}")
    else:
        print("No reservation found")
    conn.close()

def main():
    create_reservations_table()
    while True:
        print("1. Make a reservation")
        print("2. Check reservation")
        print("3. Show all reservations")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            make_reservation()
        elif choice == "2":
            check_reservation()
        elif choice == "3":
            show_all_reservations()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()