MovieMatrix

MovieMatrix is a command-line interface (CLI) movie rental system built with Python. The application allows users to manage a movie rental system, including stores, movies, and customers. The project uses SQLAlchemy ORM for database management, supporting CRUD operations, and provides a simple and interactive CLI for managing rentals and viewing available movies.

## Features

- Store Management: Add and manage stores and their inventory of movies.
- Movie Management: Add, remove, and manage movies in stores.
- Customer Management: Add customers and manage their movie rentals.
- Rentals: Keep track of which customer is renting which movie.
- CLI Interaction: Simple and interactive command-line interface for users to perform operations.

## Project Structure

```bash
MovieMatrix/
│
├── alembic/                # Alembic migrations folder
├── 
│   ├──         # App initialization and database configuration
│   ├── models.py           # SQLAlchemy ORM models for Store, Movie, Customer, base
│   ├── Debug.py              # Command-line interface logic
│   ├── db.py         # Database creation and connection logic

│
├── alembic.ini             # Alembic migration configuration file
├── Pipfile                 # Pipenv dependencies file
├── README.md               # Project README file
├── Pipfile.lock            # Pipenv lock file
```

## Installation

To run the `MovieMatrix` application, follow the steps below:

1.Clone the Repository:
   ```bash
   git clone https://github.com/peninah713/MovieMatrix.git
   ```

2. Navigate into the Project Directory:
   ```bash
   cd MovieMatrix
   ```

3. Create and Activate a Virtual Environment:
   Use `Pipenv` to create a virtual environment and install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

4. Initialize the Database:
   Run Alembic migrations to create the required database tables:
   ```bash
   alembic upgrade head
   ```

5. Run the Application:
   Start the CLI application:
   ```bash
   python debug.py
   ```

## Usage

Once the application is running, the CLI will provide you with a menu to manage stores, movies, and customers. Some available commands:

- Add a Store: Create a new store to manage its movie inventory.
- Add/Remove Movies: Add movies to a store’s inventory or remove them.
- Add a Customer: Register a customer who can rent movies.
- Rent a Movie: Rent a movie to a customer.
- View Available Movies: See which movies are available for rent.
- Return a Movie: Mark a movie as returned by a customer.

Simply follow the prompts in the terminal to perform actions.

## Dependencies

This project uses the following Python packages:

- SQLAlchemy: ORM for database management.
- Alembic: For database migrations.

---

