import uuid
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from app.verifier.shared_db.db import Base

class TaskData(Base):
    __tablename__ = "task_data"

    unic_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_type = Column(String)
    task_id = Column(Integer)
    date = Column(String)
    r_num = Column(String)
    sum = Column(Float)