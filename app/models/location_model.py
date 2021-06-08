from sqlalchemy import Column, Integer, String, DateTime
from config.azuresql import Base
import datetime

class Location(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key = True)
    
    # Information about the person and the group he is in
    sar_project_name = Column(String, nullable=False)
    sar_name = Column(String, nullable=False)
    sar_group = Column(String, nullable=False)
    
    # Last known location of the person
    sar_longitude = Column(String, nullable=False)
    sar_latitude = Column(String, nullable=False)
    
    # Time when the location was found
    sar_date_ping = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def __init__(self, sar_project_name, sar_name, sar_group, sar_longitude, sar_latitude):
        self.sar_project_name = sar_project_name
        self.sar_name = sar_name
        self.sar_group = sar_group
        self.sar_longitude = sar_longitude
        self.sar_latitude = sar_latitude