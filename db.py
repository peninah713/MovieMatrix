from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.store import Store
from models.movie import Movie
from models.customer import Customer

# SQLite database URL (can be changed for other database systems, e.g., PostgreSQL)
DATABASE_URL = 'sqlite:///movie_matrix_system.db'

# Create an engine that represents the core interface to the database
engine = create_engine(DATABASE_URL)

# Sessionmaker factory that generates new sessions for querying the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create all tables
def create_db():
    Base.metadata.create_all(engine)

