from schema import location_schema

from crud import location_crud
from typing import List
#from fastapi import Depends,HTTPException
#import json

def EnableLocationRoute(app):
    
    # Gets all locations in database
    @app.get("/locations",
    response_model=List[location_schema.Location],
    tags=["location"],
    summary="Shows all locations in database",
    response_description="Locations have been displayed"
    )
    def get_all_locations():
        """
            Get all locations:
            - **Details** : Returns all locations
        """
        return location_crud.get_all_locations()


    # Create a location in database
    @app.post("/location",
    response_model=location_schema.LocationBase,
    tags=["location"],
    summary="Create a location",
    response_description="Location has been created"
    )
    def create_plan(location_data: location_schema.LocationBase):
        """
            Get all plans:
            - **Details** : Returns location created
        """
        location = location_crud.create_plan(location_data = location_data)
        return location
