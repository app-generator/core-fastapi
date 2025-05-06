# [Getting Started with FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html)

Coding sample for **[Getting Started with FastAPI documentation page](https://app-generator.dev/docs/technologies/fastapi/index.html)**.  A simple FastAPI project demonstrating JWT authentication with token-based access. This project includes endpoints for user sign-up, login, and accessing secure and public data.

> 👉 For more [FastAPI Resources](https://app-generator.dev/docs/technologies/fastapi.html) please access:

- [Getting Started with FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html)
- [FastAPI Cheatsheet](https://app-generator.dev/docs/technologies/fastapi/cheatsheet.html)   

<br />

## Prerequisites

- Python 3.7+
- `pip` for package management

**Install dependencies**:

   ```bash
   pip install fastapi sqlalchemy pydantic passlib[bcrypt] python-jose uvicorn
   ```

<br />

## Setting Up the Database

This project uses SQLite for the database.

1. **Create Database and Tables**:

When you run the project the database and table would automatically be created.

<br />

## Running the Project

To start the FastAPI server, use the following command:

```bash
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

<br />

## API Endpoints

### 1. **Sign Up** - `/signup`

Registers a new user with a `username` and `password`.

- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/signup`
- **Request Body**:
  
  ```json
  {
    "username": "newuser",
    "password": "newpassword"
  }
  ```

- **Example**:

  ```bash
  curl -X POST "http://127.0.0.1:8000/signup" \
  -H "Content-Type: application/json" \
  -d '{
      "username": "newuser",
      "password": "newpassword"
  }'
  ```

<br />

### 2. **Login** - `/token`

Authenticates a user and returns a JWT token.

- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/token`
- **Request Body (Form Data)**:

  | Key       | Value       |
  |-----------|-------------|
  | username  | `username`  |
  | password  | `password`  |

- **Example**:

  ```bash
  curl -X POST "http://127.0.0.1:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=newuser&password=newpassword"
  ```

- **Response**:

  ```json
  {
    "access_token": "your_jwt_token",
    "token_type": "bearer"
  }
  ```

<br />

### 3. **Get Secure Data** - `/secure-data`

Returns secure data and requires a valid JWT token for access.

- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/secure-data`
- **Headers**:

  ```http
  Authorization: Bearer YOUR_ACCESS_TOKEN
  ```

- **Example**:

  ```bash
  curl -X GET "http://127.0.0.1:8000/secure-data" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
  ```

- **Response**:

  ```json
  {
    "msg": "Hello, newuser. You have access to secure data!"
  }
  ```

<br />

### 4. **Get Public Data** - `/public`

An open endpoint that does not require authentication.

- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/public`

- **Example**:

  ```bash
  curl -X GET "http://127.0.0.1:8000/public"
  ```

- **Response**:

  ```json
  {
    "msg": "This is a public route!"
  }
  ```

<br />

## Project Structure

```
.
├── main.py           # Main FastAPI application
├── models.py         # Pydantic and SQLAlchemy models
├── auth.py           # Authentication functions (JWT)
├── database.py       # Database configuration and session management
└── README.md         # Project documentation
```

<br />

## Dependencies

- `fastapi` - Web framework for building APIs.
- `sqlalchemy` - ORM for interacting with SQLite database.
- `pydantic` - Data validation for request and response models.
- `passlib[bcrypt]` - Password hashing library.
- `python-jose` - For handling JWT encoding and decoding.
- `uvicorn` - ASGI server for FastAPI.

<br />

## Notes

- Replace `"YOUR_ACCESS_TOKEN"` in `curl` examples with the actual token obtained from the login endpoint.
- Update `DATABASE_URL` in `database.py` if you switch to another database (e.g., PostgreSQL).
- To access Swagger documentation, visit: `http://127.0.0.1:8000/docs`.

<br />

---
**[Getting Started with FastAPI](https://app-generator.dev/docs/technologies/fastapi/index.html)** - Coding sample provided by **[App Generator](https://app-generator.dev/)** 
