"""Database base configuration.

Uncomment and configure when adding SQLAlchemy.
"""

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from app.core.config import settings

# Base = declarative_base()

# engine = create_engine(
#     settings.DATABASE_URL,
#     connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
# )


# Placeholder for when database is not yet configured
class Base:
    """Placeholder base class."""
    pass
