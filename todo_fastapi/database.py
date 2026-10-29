import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from decouple import config


load_dotenv()
# url=URL.create(
#     drivername="postgresql",
#     username="postgres",
#     password="",
#     host="localhost",
#     database="mydb",
#     port=5432
# )

url=config("POSTGRES_DB_URL")

engine=create_engine(url) # type: ignore
Session=sessionmaker(bind=engine)
session=Session()