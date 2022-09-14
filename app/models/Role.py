from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from app.database import BaseClassDB


class Role(BaseClassDB):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationships:
    # user_id = Column(Integer, ForeignKey('user.id'))

    def __str__(self):
        return f"{self.email} ({self.first_name} {self.last_name}) - {self.public_id}"

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description
        )
