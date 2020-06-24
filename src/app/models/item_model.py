from sqlalchemy import String, Column

from app.db.db import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(String, primary_key=True)
    is_superadmin = Column(String)
    is_faculty = Column(String)
