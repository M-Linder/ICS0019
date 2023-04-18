import datetime

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to the database and declare the tables.
engine = create_engine("sqlite:///canteens.db", echo=False)

Base = declarative_base()


class Provider(Base):
    # Table for restaurant owners/providers.
    # Contains two fields. ID and provider name.
    __tablename__ = "PROVIDER"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)


class Canteen(Base):
    # Table for canteens.
    # Contains 6 fields. ID, Affiliated Provider ID, Name, Location, Opening Time, Closing Time.
    __tablename__ = "CANTEEN"

    Id = Column(Integer, primary_key=True)
    ProviderID = Column(Integer)
    Name = Column(String)
    Location = Column(String)
    time_open = Column(String)
    time_closed = Column(String)


# Declare all the specified tables and start a new database session.
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    # Query the database for Canteens belonging to the specified provider.
    result = session.query(Canteen, Provider).filter(
        Provider.Name == "Baltic Restaurants Estonia AS",
        Canteen.ProviderID == Provider.Id,
    )

    # Print the result in a list.
    print("\n\nCANTEENS THAT ARE PROVIDED BY: Baltic Restaurants Estonia AS")
    for row in result:
        print(
            "Canteen:",
            row[0].Name,
            "\nProvider:",
            row[1].Name,
        )

    # Query the database for Canteens that are open in the specified time frame.
    result = session.query(Canteen).filter(
        Canteen.time_open <= datetime.time(9, 0),
        Canteen.time_closed >= datetime.time(16, 20),
    )

    # Print the result in a list.
    print("\n\nCANTEENS THAT ARE OPEN BETWEEN 9:00 AND 16:20")
    for row in result:
        print(
            "Name: ",
            row.Name,
            "Location: ",
            row.Location,
            "\n",
            "Opens: ",
            row.time_open,
            "Closes: ",
            row.time_closed,
        )

except Exception:
    # Rollback to original state if exception occurs.
    raise Exception

finally:
    # Close the session.
    session.close()
