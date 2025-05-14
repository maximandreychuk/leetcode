from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "sqlite.db"
engine = create_engine(db_url)
session = sessionmaker(bind=engine)
