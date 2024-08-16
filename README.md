# Data Ingestion API

## Overview
This API allows users to upload CSV files and retrieve basic summary statistics for numerical columns.

## Endpoints

### 1. Upload CSV File
- **URL:** `/api/upload/`
- **Method:** `POST`
- **Headers:**
  - `API-KEY: mysecretkey`
- **Body:** `multipart/form-data` with the CSV file
- **Response:**
  - `201 Created` on success
  - `400 Bad Request` if the file is not a valid CSV or is empty

### 2. Retrieve Summary Statistics
- **URL:** `/api/statistics/`
- **Method:** `GET`
- **Headers:**
  - `API-KEY: mysecretkey`
- **Response:** JSON object with summary statistics for numerical columns.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/data-ingestion-api.git
   cd data-ingestion-api

2. ## Create a Virtual Environment (optional but recommended):
  python -m venv env
  source env/bin/activate  # On Windows use `env\Scripts\activate`

3. ## Install Dependencies:
  pip install -r requirements.txt

4. ##   Migrations:
  python manage.py migrate

5. ##  Create a Superuser (optional, for Django admin access):
  python manage.py createsuperuser

6. ## Run the Server:
  python manage.py runserver


7. ## Access the API:
  Upload CSV File:
  Use curl or Postman to send a POST request to http://127.0.0.1:8000/api/upload/ with the file and API key.

  bash
  Copy code
            curl --location 'http://127.0.0.1:8000/api/upload/' \
            --header 'API-KEY: mysecretkey' \
            --form 'file=@"/path/to/your/file.csv"'
  Retrieve Summary Statistics:
  Use curl or Postman to send a GET request to http://127.0.0.1:8000/api/statistics/ with the API key.

  bash
  Copy code
          curl --location 'http://127.0.0.1:8000/api/statistics/' \
          --header 'API-KEY: mysecretkey'