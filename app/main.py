from typing import Optional
from fastapi import FastAPI
from config.azuresql import SessionLocal, Base

app = FastAPI()
session = SessionLocal()

mydata = [{"name": "Windows 2012 R2","sku": "win2012"},{"name": "Windows 2016","sku": "win2016"},{"name": "Windows 2019","sku": "win2019"}]

@app.get("/")
def read_os():
   
    return {"mydata": "bleh"}
    

@app.get("/os/{os_sku}", 
tags=["items"],
summary="This displays an operating system sku",
#description="Something Something Dark Side",
response_description="I searched the item")
async def read_os(os_sku):
    """
    Get item with os information:

    - **os_sku**: You must provide a os_sku parameter
    """
    return {"os_sku": os_sku}
