from models.store import Store
from models.movie import Movie
from models.customer import Customer
from db import session  # Import the session from db.py

def add_store():
    name = input("Enter store name: ")
    location = input("Enter store location: ")
    store = Store.create(session, name, location)
    session.commit()
    print(f"Store '{name}' added.")

def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    store_id = int(input("Enter store ID: "))
    
    # Use session.get() to fetch the store by ID
    store = session.get(Store, store_id)

    if not store:
        print(f"No store found with ID {store_id}.")
        return

    # Create and add movie to the store
    movie = Movie.create(session, title, genre, store)
    session.commit()  # Commit the transaction to persist changes

    print(f"Movie '{title}' added to store '{store.name}'.")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    customer = Customer.create(session, name, email)
    session.commit()
    print(f"Customer '{name}' added.")

def main():
    while True:
        print("\n=== Movie Rental System ===")
        print("1. Manage Stores")
        print("2. Manage Movies")
        print("3. Manage Customers")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_store()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            add_customer()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
