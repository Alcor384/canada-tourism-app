# canada-tourism-app
Canada Tourism Spot Ranking Platform

# Canada Tourism Spot Ranking Platform

A full-stack web application to browse, rate, and review popular tourism spots across Canada.  
Users can register, login, add their favorite spots to their collections, rate and comment on spots, and view rankings based on ratings and popularity.

---

## Tech Stack

- **Frontend:** React.js with React Router and Axios  
- **Backend:** FastAPI with SQLAlchemy ORM  
- **Database:** PostgreSQL  
- **Authentication:** JWT token-based auth  
- **Hosting:** Local development (Docker support for future deployment)

---

## Features

- User registration and authentication  
- Browse popular Canadian tourism spots with detailed info  
- Add spots to favorites  
- Rate and write comments on spots  
- Like and reply to comments  
- Rankings by average rating or number of favorites  
- Pagination and search filters  

---

## Getting Started

### Prerequisites

- Python 3.9+  
- Node.js 16+  
- PostgreSQL (or use Docker for local setup)  

### Backend Setup

1. Create and activate Python virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure database URL in `.env` file:
    ```
    DATABASE_URL=postgresql://username:password@localhost:5432/tourismdb
    ```

4. Run migrations and start the FastAPI server:
    ```bash
    alembic upgrade head
    uvicorn main:app --reload
    ```

### Frontend Setup

1. Navigate to frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start React development server:
    ```bash
    npm start
    ```

4. Access app at [http://localhost:3000](http://localhost:3000)

---

## Project Structure
/backend
/app
main.py
models.py
schemas.py
routers/
database.py
/frontend
/src
components/
pages/
services/
App.jsx


---

## Future Improvements

- Integrate OpenTripMap API for real-time spot data  
- Add social login (Google, Facebook)  
- Add real-time notifications for comments and likes  
- Deploy with Docker and CI/CD pipeline  
- Implement advanced recommendation engine  

---

## License

MIT License

---

## Contact

Created by Alcor Li - feel free to connect!



