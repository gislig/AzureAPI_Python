from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.azuresql import SessionLocal, Base, engine
from models import location_model
from routes import location_route

session = SessionLocal()
Base.metadata.create_all(engine)

app = FastAPI(
    title = "Landsbjörg SAR environment",
    version = "1.0",
    debug = True
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

location_route.EnableLocationRoute(app)