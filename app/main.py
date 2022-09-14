import uvicorn
from app import app

# import database models:
from app.database import engine
from models import User, Role

# import endpoints
from app.endpoints import UserEndpoint

# generate automatically tables in database:
User.BaseClassDB.metadata.create_all(bind=engine)
Role.BaseClassDB.metadata.create_all(bind=engine)

# To include EndPoints:
app.include_router(UserEndpoint.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
