from pydantic import BaseModel

class LocationBase(BaseModel):
    sar_project_name: str
    sar_name: str
    sar_group: str
    sar_longitude: str
    sar_latitude: str

class Location(LocationBase):
    sar_date_ping: str

    class Config:
        orm_mode = True