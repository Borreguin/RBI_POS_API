import os
import sys
from fastapi import FastAPI
from app.database import SessionLocal, engine, BaseClassDB

# To include the project path in the Operating System path:
script_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(script_path)
sys.path.append(project_path)

# FastApi Framework
app = FastAPI()


# Define Database connection
def local_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
