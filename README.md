Project Overview
The Concert Management System models the relationship between Bands, Venues, and Concerts. It establishes a many-to-many relationship between Bands and Venues via Concerts. The system tracks:
    Bands and their hometowns
    Venues and their locations
    Concerts, which associate bands and venues with performance dates
Prerequisites
Before you begin, ensure you have the following installed:
    [a]Python 3.x
    [b]SQLite (pre-installed with most Python setups)
    [c]SQLAlchemy (pip install SQLAlchemy)
    [d]A terminal/command-line interface for running the program
Installation
Clone this repository to your local machine:
git clone https://github.com/yourusername/concert-management.git
Navigate to the project directory:
cd concert-management
Install the required dependencies:
pip install -r requirements.txt
Create the SQLite database:
    python3 models.py
Database Models
The project uses SQLAlchemy ORM to manage the following database models:
Band
    name (String) - Name of the band
    hometown (String) - Hometown of the band
Venue
    title (String) - Name of the venue
    city (String) - City where the venue is located
Concert
    date (String) - Date of the concert
    band_id (ForeignKey) - Associated band ID (links to the Band model)
    venue_id (ForeignKey) - Associated venue ID (links to the Venue model)
The many-to-many relationship between Band and Venue is modeled via Concerts.
Features
Band Features
    concerts() - Returns all concerts performed by a band
    venues() - Returns all venues where the band has performed
    play_in_venue(venue, date) - Creates a new concert for the band at the specified venue on the given date
    all_introductions() - Returns a list of all concert introductions for the band
    most_performances() (class method) - Returns the band with the most concerts
Venue Features
    concerts() - Returns all concerts held at the venue
    bands() - Returns all bands that have performed at the venue
    concert_on(date) - Finds the first concert held at the venue on a given date
    most_frequent_band() - Returns the band that has performed the most at the venue
Concert Features
    band() - Returns the band instance associated with the concert
    venue() - Returns the venue instance associated with the concert
    hometown_show() - Returns True if the concert is in the band's hometown, False otherwise
    introduction() - Returns a formatted introduction string for the band at the concert
Running the Application
Ensure you have run the migration to create the necessary tables in the database:
python3 models.py
Open the Python shell or run a Python script to test the database:
python3
You can now add bands, venues, and concerts to the system. For example:
    from models import session, Band, Venue, Concert
    # Create new band and venue
    band = Band(name="The Rolling Stones", hometown="London")
    venue = Venue(title="Madison Square Garden", city="New York")
    session.add(band)
    session.add(venue)
    session.commit()
    # Create a concert
    concert = Concert(band_id=band.id, venue_id=venue.id, date="2024-10-10")
    session.add(concert)
    session.commit()
    # Query data
    print(concert.introduction())  # Output: "Hello New York!!!!! We are The Rolling Stones and we're from London"
Example Queries
Here are some example queries you can run to retrieve data from the system:
Get all concerts for a specific band:
band = session.query(Band).first()
print(band.concerts())
Find the band with the most performances:
print(Band.most_performances())
Get all venues where a band has performed:
print(band.venues())
Get all bands that have performed at a specific venue:
    venue = session.query(Venue).first()
    print(venue.bands())
License:
This project is licensed under the MIT License - see the LICENSE file for details.
