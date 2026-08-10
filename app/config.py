
# this file is about environments variable
# this is for database path Url
from pydantic_settings import BaseSettings

class settings(BaseSettings):
    sql_url = "sqlite:///D:/work projects/alembic_works/app/database.db"

setting = settings()
