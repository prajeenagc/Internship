import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


load_dotenv()
# url=URL.create(
#     drivername="postgresql",
#     username="postgres",
#     password="",
#     host="localhost",
#     database="mydb",
#     port=5432
# )

url=os.getenv("POSTGRES_DB_URL")

engine=create_engine(url)
Session=sessionmaker(bind=engine)
session=Session()