# Lab Results API

FastAPI-based API for managing laboratory test results, patient data, and related information. Supports creating, retrieving, updating, and deleting patient and test data.

## Features
- CRUD operations for patients, tests, and results
- RESTful API endpoints
- Swagger UI for testing API
- File uploads for test results (e.g., scanned reports)

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/rubaabueisa/lab-results-cloud.git


Navigate to the project folder:

cd lab-results-cloud


Set up the virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Run the FastAPI application:

uvicorn app.main:app --host 0.0.0.0 --port 8000


Access the API docs:

http://127.0.0.1:8000/docs

Technologies Used

FastAPI, SQLAlchemy, SQLite, Pydantic, Uvicorn

Future Enhancements

Authentication & Authorization

AWS S3 integration for file storage

Support for PostgreSQL or MySQL

License

MIT License
