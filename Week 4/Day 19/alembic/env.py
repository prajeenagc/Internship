from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.database import Base
from app.config import settings
from app.models import User, Task


config = context.config

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata