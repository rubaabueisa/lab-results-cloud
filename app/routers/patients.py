from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.PatientOut)
def create_patient(patient: schemas.PatientBase, db: Session = Depends(database.get_db)):
    db_patient = models.Patient(name=patient.name, dob=patient.dob)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=list[schemas.PatientOut])
def get_patients(db: Session = Depends(database.get_db)):
    return db.query(models.Patient).all()

@router.get("/{patient_id}", response_model=schemas.PatientOut)
def get_patient(patient_id: int, db: Session = Depends(database.get_db)):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
