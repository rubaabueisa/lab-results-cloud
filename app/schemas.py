from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatientBase(BaseModel):
    name: str
    dob: Optional[datetime] = None

class PatientOut(PatientBase):
    id: int

    class Config:
        orm_mode = True

class TestBase(BaseModel):
    name: str
    unit: Optional[str] = None
    normal_range: Optional[str] = None

class TestOut(TestBase):
    id: int

    class Config:
        orm_mode = True

class ResultBase(BaseModel):
    value: Optional[float] = None
    status: Optional[str] = "final"
    patient_id: int
    test_id: int

class ResultOut(ResultBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
