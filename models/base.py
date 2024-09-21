# Importing declarative_base, which is used to define the base class for our models.
from sqlalchemy.ext.declarative import declarative_base

# Base is used as a foundation for all models.
# All model classes will inherit from this base class.
Base = declarative_base()
