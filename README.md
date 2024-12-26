# Airport API ✈️🌍

This is a DRF project for managing various components of an airport, including airplane types, airplanes, airports, crews, flights, orders, and routes. The API supports authentication and user management and provides detailed documentation via Redoc and Swagger.

## Project structure 📊
![image](https://github.com/user-attachments/assets/4aba7db1-d24c-48f4-a31f-747c4e537d2b)

## Features ✨

- **API Endpoints** for managing:
  - Airplane Types
  - Airplanes
  - Airports
  - Crews
  - Flights
  - Orders
  - Routes
- **User Authentication**:
  - User registration
  - JWT authentication
- **API Documentation** - Redoc and Swagger
- **Database Management** - PostgreSQL
- **Code Linting** - Ruff
- **Containerized Deployment** - Docker and Docker Compose

## Technologies used ⚙️

- **Backend**: Python 3.12, Django 5.1.4, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Simple JWT
- **Linting**: Ruff
- **Containerization**: Docker, Docker Compose
- **Environment Management**: Poetry, Python-dotenv

---

## Getting Started 🐾

### Prerequisites

- Python 3.12+
- Poetry
- Docker and Docker Compose
- Make

### Local Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/dxrrkwm/airport-api.git
cd airport-api
```

#### 2. Create a `.env` File
Fill in the `.env` file, use `.env.template` as a reference to that.

#### 3. Install Dependencies
Run the following command to install dependencies using Poetry:
```bash
make deps
```

#### 4. Apply Migrations
Run database migrations:
```bash
make migrate
```

#### 5. Start the Development Server
Start the Django development server:
```bash
make run
```

The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### Running with Docker

#### 1. Build and Start the Services
Use Docker Compose to build and run the application and database:
```bash
docker-compose up --build
```

#### 2. Access the API
- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- The PostgreSQL database will be available on port `5432`.

---

## Makefile Commands

- `make deps`: Install dependencies using Poetry.
- `make run`: Run the development server.
- `make migrate`: Apply migrations.
- `make makemigrations`: Create new migrations.
- `make lint`: Run code linting with Ruff.
- `make clean`: Remove `__pycache__` directories.

---

## API Endpoints 🧩

Below is a list of the available API endpoints:

### Airplane Types
- `GET /api/airport/airplane_types/`
- `POST /api/airport/airplane_types/`
- `GET /api/airport/airplane_types/<id>/`
- `PUT /api/airport/airplane_types/<id>/`
- `PATCH /api/airport/airplane_types/<id>/`
- `DELETE /api/airport/airplane_types/<id>/`

### Airplanes
- `GET /api/airport/airplanes/`
- `POST /api/airport/airplanes/`
- `GET /api/airport/airplanes/<id>/`
- `PUT /api/airport/airplanes/<id>/`
- `PATCH /api/airport/airplanes/<id>/`
- `DELETE /api/airport/airplanes/<id>/`

### User Management
- `POST /api/users/register/`: Register a new user.
- `POST /api/users/token/`: Obtain a JWT token.
- `POST /api/users/token/refresh/`: Refresh a JWT token.
- `POST /api/users/token/verify/`: Verify a JWT token.
- `GET /api/users/profile/`: Retrieve user profile.
- `PUT /api/users/profile/`: Update user profile.

### (Other resources follow similar patterns)

## Linting

Run the Ruff linter:
```bash
make lint
```

## Documentation 📄

API documentation is available via Redoc at:
```
http://127.0.0.1:8000/redoc/
```
and via Swagger at:
```
http://127.0.0.1:8000/api/doc/swagger/
```
---

