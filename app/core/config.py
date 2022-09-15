"""
Global settings for the application
"""
from dotenv import load_dotenv
import os
from app import project_path

environment = os.getenv('ENV', 'dev')
if environment == 'prod':
    env_path = os.path.join(project_path, 'core', 'dev.env')
else:
    env_path = os.path.join(project_path, 'core', 'prod.env')

load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Not defined")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION", "0.0.0")


settings = Settings()
