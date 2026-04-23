from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.database import Base
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    phone = Column(String, unique=False)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    