from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from todo.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todo = relationship("Todo", backref="users")

class Todo(Base):
    __tablename__ = "routine"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status_completed = Column("completed", Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    #users = relationship("User", backref="routine")
