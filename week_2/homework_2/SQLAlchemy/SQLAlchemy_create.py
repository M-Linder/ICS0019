import datetime
import os.path

from sqlalchemy import Time
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# If the database file exists, remove it for a fresh start.
if os.path.exists("canteens.db"):
    os.remove("canteens.db")

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
    ProviderID = Column(Integer, ForeignKey("PROVIDER.Id"))
    Name = Column(String)
    Location = Column(String)
    time_open = Column(Time)
    time_closed = Column(Time)


# Declare all the specified tables and start a new database session.
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    # Insert providers into the database.
    session.add_all(
        [
            Provider(Name="Rahva Toit"),
            Provider(Name="Baltic Restaurants Estonia AS"),
            Provider(Name="TTÜ Sport OÜ"),
        ]
    )

    # Insert canteens into the database.
    session.add_all(
        [
            Canteen(
                Name="Economics- and social science building canteen",
                Location="Akadeemia tee 3, SOC- building",
                ProviderID=1,
                time_open=datetime.time(8, 30),
                time_closed=datetime.time(19, 0),
            ),
            Canteen(
                Name="Library canteen",
                Location="Akadeemia tee 1/Ehitajate tee 7",
                ProviderID=1,
                time_open=datetime.time(8, 30),
                time_closed=datetime.time(19, 0),
            ),
            Canteen(
                Name="Main building Deli cafe",
                Location="Ehitajate tee 5, U01 building",
                ProviderID=2,
                time_open=datetime.time(9, 0),
                time_closed=datetime.time(16, 30),
            ),
            Canteen(
                Name="Main building Daily lunch restaurant",
                Location="Ehitajate tee 5, U01 building",
                ProviderID=2,
                time_open=datetime.time(9, 0),
                time_closed=datetime.time(16, 30),
            ),
            Canteen(
                Name="U06 building canteen",
                Location="Ehitajate tee 5, U06 building",
                ProviderID=1,
                time_open=datetime.time(9, 0),
                time_closed=datetime.time(16, 0),
            ),
            Canteen(
                Name="Natural Science building canteen",
                Location="Akadeemia tee 15, SCI building",
                ProviderID=2,
                time_open=datetime.time(9, 0),
                time_closed=datetime.time(16, 0),
            ),
            Canteen(
                Name="ICT building canteen",
                Location="Raja 15/Mäepealse 1",
                ProviderID=2,
                time_open=datetime.time(9, 0),
                time_closed=datetime.time(16, 0),
            ),
            Canteen(
                Name="Sports building canteen",
                Location="Männiliiva 7, S01 building",
                ProviderID=3,
                time_open=datetime.time(11, 0),
                time_closed=datetime.time(20, 0),
            ),
        ]
    )

    # ITCollege provider and canteen inserted separately.
    session.add(Provider(Name="Bitt OÜ"))
    session.add(
        Canteen(
            Name="bitStop KOHVIK",
            Location="IT College, Raja 4c",
            ProviderID=4,
            time_open=datetime.time(9, 30),
            time_closed=datetime.time(16, 0),
        )
    )

    # Commit changes to the database.
    session.commit()

except Exception:
    # Rollback to original state if exception occurs.
    session.rollback()
    raise Exception

finally:
    # Close the session.
    session.close()
