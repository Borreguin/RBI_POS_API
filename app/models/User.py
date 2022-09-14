from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import BaseClassDB
import uuid


class User(BaseClassDB):
    __tablename__ = 'user'
    # Fields:
    id = Column(Integer, primary_key=True, index=True)
    public_id = Column(String, unique=True, index=True, default=None)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationships:
    # roles = relationship('Role', backref='user')

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        if self.public_id is None:
            self.public_id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.email} ({self.first_name} {self.last_name}) - {self.public_id}"

    def to_dict(self):
        return dict(
            public_id=self.public_id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )
