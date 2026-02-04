
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    doctor_language = Column(String)
    patient_language = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    role = Column(String)
    original_text = Column(Text, nullable=True)
    translated_text = Column(Text, nullable=True)
    audio_path = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
