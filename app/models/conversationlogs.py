from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.db.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=True)
    channel = Column(String, default="web")
    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=True)
    intent = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient")