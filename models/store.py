from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Store(Base):
    # Define table name for SQLAlchemy ORM
    __tablename__ = 'stores'  

    # Define columns for the stores table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # Relationship between Store and Movies (One-to-many)
    # Each store can have multiple movies, and if a store is deleted, its movies are also deleted.
    movies = relationship('Movie', back_populates='store', cascade='all, delete-orphan')

    # Constructor to initialize a Store object
    def __init__(self, name, location=None):
        self.name = name
        self.location = location

    # ORM method to create a new store and save it to the database
    @classmethod
    def create(cls, session, name, location=None):
        store = cls(name, location)
        session.add(store)  # Add store object to session
        session.commit()    # Commit to the database
        return store

    # ORM method to delete a store from the database
    @classmethod
    def delete(cls, session, store_id):
        store = session.query(cls).filter_by(id=store_id).first()
        if store:
            session.delete(store)  # Remove store object from session
            session.commit()

    # ORM method to get all stores from the database
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    # ORM method to find a specific store by its ID
    @classmethod
    def find_by_id(cls, session, store_id):
        return session.query(cls).filter_by(id=store_id).first()

    # Method to add a movie to the store's movie list
    def add_movie(self, movie):
        self.movies.append(movie)
