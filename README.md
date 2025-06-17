# 🚀 FastAPI CRUD with PostgreSQL and Authentication

This repository contains a FastAPI application that implements **CRUD operations** with **PostgreSQL** as the database, along with **user authentication and validation features**.

## 🧰 Features

- ✅ FastAPI framework for high-performance APIs
- 🗃️ PostgreSQL for robust relational data management
- 🔐 User login validation with hashed password authentication
- 🔄 CRUD operations (Create, Read, Update, Delete)
- 📦 Modular project structure
- 🧪 Input validation using Pydantic models
- 🛡️ Security features using OAuth2 and JWT tokens

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/18Prashanth/FastAPI_CRUD_Operation.git

cd FastAPI_CRUD_Operation
```

### 2. Create and Activate Virtual Environment

```
python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Environment Variables

```
DATABASE_URL=postgresql://username:password@localhost/dbname

SECRET_KEY=your_secret_key
```

### 5. Run the Application

uvicorn app.main:app --reload

🔑 API Authentication

- Register user via /register

- Login via /login (returns JWT token)

- Use the token in headers for protected routes:

Authorization: Bearer <your_token_here>
