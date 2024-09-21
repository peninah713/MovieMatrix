from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Customer(Base):
    # Define table name for SQLAlchemy ORM
    __tablename__ = 'customers'  

    # Define columns for the customers table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Foreign key to relate customers to movies they rent
    movie_id = Column(Integer, ForeignKey('movies.id'))

    # Relationship between Customer and Movie (Many-to-one)
    # Each customer rents one movie, and a movie can be rented by many customers over time.
    movie = relationship('Movie', back_populates='customers')

    # Constructor to initialize a Customer object
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # ORM method to create a new customer and save it to the database
    @classmethod
    def create(cls, session, name, email):
        customer = cls(name, email)
        session.add(customer)  # Add customer object to session
        session.commit()       # Commit to the database
        return customer

    # ORM method to delete a customer from the database
    @classmethod
    def delete(cls, session, customer_id):
        customer = session.query(cls).filter_by(id=customer_id).first()
        if customer:
            session.delete(customer)  # Remove customer object from session
            session.commit()

    # ORM method to get all customers from the database
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    # ORM method to find a specific customer by their ID
    @classmethod
    def find_by_id(cls, session, customer_id):
        return session.query(cls).filter_by(id=customer_id).first()

    # Method for a customer to rent a movie
    def rent_movie(self, movie):
        if movie.availability:  # Check if the movie is available
            self.movie = movie
            movie.update_availability(False)  # Mark the movie as unavailable

    # Method for a customer to return a rented movie
    def return_movie(self):
        if self.movie:  # Ensure the customer has rented a movie
            self.movie.update_availability(True)  # Mark the movie as available again
            self.movie = None  # Remove the movie from the customer's rental
