from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Movie(Base):
    # Define table name for SQLAlchemy ORM
    __tablename__ = 'movies'  

    # Define columns for the movies table
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    availability = Column(Boolean, default=True)  # True means available for rental

    # Foreign key to relate movies to stores
    store_id = Column(Integer, ForeignKey('stores.id'))

    # Relationship between Movie and Store (Many-to-one)
    # A movie belongs to one store, and the store can have many movies.
    store = relationship('Store', back_populates='movies')

    # Relationship between Movie and Customer (One-to-many)
    # One movie can be rented by many customers over time.
    customers = relationship('Customer', back_populates='movie')

    # Constructor to initialize a Movie object
    def __init__(self, title, genre, store):
        self.title = title
        self.genre = genre
        self.store = store

    # ORM method to create a new movie and save it to the database
    @classmethod
    def create(cls, session, title, genre, store):
        movie = cls(title, genre, store)
        session.add(movie)  # Add movie object to session
        session.commit()    # Commit to the database
        return movie

    # ORM method to delete a movie from the database
    @classmethod
    def delete(cls, session, movie_id):
        movie = session.query(cls).filter_by(id=movie_id).first()
        if movie:
            session.delete(movie)  # Remove movie object from session
            session.commit()

    # ORM method to get all movies from the database
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    # ORM method to find a specific movie by its ID
    @classmethod
    def find_by_id(cls, session, movie_id):
        return session.query(cls).filter_by(id=movie_id).first()

    # Method to update the availability status of a movie
    def update_availability(self, available):
        self.availability = available
