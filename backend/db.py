# filepath: c:\Users\PAULO LAB ITEGAM\Desktop\PAULO\teste\backend\db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")

# Use o driver mariadb
DATABASE_URL = f"mariadb+mariadbconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()