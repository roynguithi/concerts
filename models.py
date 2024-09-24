from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Base class
Base = declarative_base()

# Band model
class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    concerts = relationship('Concert', back_populates='band')

# Venue model
class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    concerts = relationship('Concert', back_populates='venue')

# Concert model
class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

# Create the SQLite database and tables
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data into the tables

# Add a band
band1 = Band(name='The Beatles', hometown='Liverpool')
band2 = Band(name='Led Zeppelin', hometown='London')
session.add(band1)
session.add(band2)

# Add a venue
venue1 = Venue(title='Madison Square Garden', city='New York')
venue2 = Venue(title='Wembley Stadium', city='London')
session.add(venue1)
session.add(venue2)

# Add concerts
concert1 = Concert(date='1969-08-15', band=band1, venue=venue1)
concert2 = Concert(date='1975-05-23', band=band2, venue=venue2)
session.add(concert1)
session.add(concert2)

# Commit the transaction to save data
session.commit()
