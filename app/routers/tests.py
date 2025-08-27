from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.TestOut)
def create_test(test: schemas.TestBase, db: Session = Depends(database.get_db)):
    db_test = models.Test(name=test.name, unit=test.unit, normal_range=test.normal_range)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

@router.get("/", response_model=list[schemas.TestOut])
def get_tests(db: Session = Depends(database.get_db)):
    return db.query(models.Test).all()
