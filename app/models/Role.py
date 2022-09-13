from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import BaseClassDB
import uuid


class Role(BaseClassDB):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationships:
    owner = relationship('UserRole', back_populates='owner')

    def __str__(self):
        return f"{self.email} ({self.first_name} {self.last_name}) - {self.public_id}"

    def to_dict(self):
        return dict(
            public_id=self.public_id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )
