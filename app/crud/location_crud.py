from config.azuresql import SessionLocal
from models import location_model
from schema.location_schema import Location

session = SessionLocal()

# Get all locations in database


def get_all_locations():
    return session.query(location_model.Location).all()

# Create location into database


def create_location(location_data: Location):
    new_location = location_model.Location(sar_project_name=location_data.sar_project_name, sar_name=location_data.sar_name, sar_group=location_data.sar_group,
                                           sar_latitude=location_data.sar_latitude, sar_longitude=location_data.sar_longitude)

    session.add(new_location)
    session.commit()
    session.refresh(new_location)

    return new_location
