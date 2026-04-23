from app.db.database import SessionLocal
from app.models.patient import Patient
from app.models.doctors import Doctor
from app.models.appointment import Appointment
from app.models.availability import DoctorAvailability
from app.models.conversationlogs import Conversation

import uuid
from datetime import time, datetime


def seed():
    db = SessionLocal()

    try:
        
        patient1 = Patient(
            id=uuid.uuid4(),
            full_name="Ahmed Raza",
            phone="03123456789",
            email="ahmed.raza@example.com"
        )

        patient2 = Patient(
            id=uuid.uuid4(),
            full_name="Fatima Noor",
            phone="03219876543",
            email="fatima.noor@example.com"
        )

        db.add_all([patient1, patient2])
        db.commit()


        doc1 = Doctor(
            id=uuid.uuid4(),
            full_name="Dr. Ali Khan",
            specialization="Cardiologist",
            phone="03001234567",
            email="ali.khan@example.com"
        )

        doc2 = Doctor(
            id=uuid.uuid4(),
            full_name="Dr. Sara Ahmed",
            specialization="Dermatologist",
            phone="03007654321",
            email="sara.ahmed@example.com"
        )

        db.add_all([doc1, doc2])
        db.commit()

        availability = [
            DoctorAvailability(
                id=uuid.uuid4(),
                doctor_id=doc1.id,
                day_of_week=0,  # Monday
                start_time=time(9, 0),
                end_time=time(14, 0)
            ),
            DoctorAvailability(
                id=uuid.uuid4(),
                doctor_id=doc1.id,
                day_of_week=2,  # Wednesday
                start_time=time(10, 0),
                end_time=time(15, 0)
            ),
            DoctorAvailability(
                id=uuid.uuid4(),
                doctor_id=doc2.id,
                day_of_week=1,  # Tuesday
                start_time=time(11, 0),
                end_time=time(16, 0)
            ),
        ]

        db.add_all(availability)
        db.commit()

        appointment1 = Appointment(
            id=uuid.uuid4(),
            patient_id=patient1.id,
            doctor_id=doc1.id,
            appointment_time=datetime(2026, 4, 25, 10, 0),
            status="scheduled",
            reason="Chest pain"
        )

        appointment2 = Appointment(
            id=uuid.uuid4(),
            patient_id=patient2.id,
            doctor_id=doc2.id,
            appointment_time=datetime(2026, 4, 26, 12, 0),
            status="scheduled",
            reason="Skin allergy"
        )

        db.add_all([appointment1, appointment2])
        db.commit()

        convo1 = Conversation(
            id=uuid.uuid4(),
            patient_id=patient1.id,
            channel="web",
            user_message="I want to book an appointment with a cardiologist",
            ai_response="Sure, booking an appointment with Dr. Ali Khan.",
            intent="book_appointment"
        )

        convo2 = Conversation(
            id=uuid.uuid4(),
            patient_id=patient2.id,
            channel="web",
            user_message="Do you have a dermatologist available?",
            ai_response="Yes, Dr. Sara Ahmed is available.",
            intent="check_availability"
        )

        db.add_all([convo1, convo2])
        db.commit()

        print(" Full seed data inserted successfully")

    except Exception as e:
        db.rollback()
        print("❌ Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed()