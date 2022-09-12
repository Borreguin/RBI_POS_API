import os
import sys
from app.database import SessionLocal

script_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(script_path)
sys.path.append(script_path)
sys.path.append(project_path)


def local_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
