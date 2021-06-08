


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder,".env"))
#print(project_folder)

server = os.getenv("MSSQLSERVER")
database = os.getenv("MSSQLDATABASE")
username = os.getenv("MSSQLUSER")
password = os.getenv("MSSQLPASS")
#print(server, database, username)
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://uteamup:" + password + "@" + server + "/" + database + "?driver=ODBC+Driver+17+for+SQL+Server"
#print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # , connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()