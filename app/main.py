from fastapi import FastAPI
from .database import Base, engine
from .routers import patients, tests

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(tests.router, prefix="/tests", tags=["tests"])
