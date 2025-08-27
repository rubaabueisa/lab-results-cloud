from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dob = Column(DateTime, nullable=True)

    results = relationship("Result", back_populates="patient")

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    unit = Column(String, nullable=True)
    normal_range = Column(String, nullable=True)

    results = relationship("Result", back_populates="test")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=True)
    status = Column(String, default="final")
    test_id = Column(Integer, ForeignKey("tests.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    created_at = Column(DateTime)

    test = relationship("Test", back_populates="results")
    patient = relationship("Patient", back_populates="results")
