from app.db.database import Base, engine
from app.models.patient import Patient
from app.models.doctors import Doctor
from app.models.appointment import Appointment
from app.models.availability import DoctorAvailability
from app.models.conversationlogs import Conversation

def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")