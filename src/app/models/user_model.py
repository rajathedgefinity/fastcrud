from sqlalchemy import String, CHAR, Column

from app.db.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(CHAR)
    create_at = Column(String)
    status = Column(CHAR)
