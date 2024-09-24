from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///concerts.db')  # Use your database URI here
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()