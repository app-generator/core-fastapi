from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_access_token, verify_password, get_password_hash, decode_token
from models import UserInDB, Token
from datetime import timedelta

app = FastAPI()

# For OAuth2 scheme (token-based authentication)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Example in-memory user database (replace with real DB in production)
fake_users_db = {
    "john": {
        "username": "john",
        "hashed_password": get_password_hash("secret"),
        "password": 'secret'
    }
}


# Dependency to get the current user based on token
def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    print(username)
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return UserInDB(**user)


# Route to get a token (authentication)
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    print("***********USERNAME", form_data.username)
    access_token = create_access_token(data={"sub": form_data.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}


# A secure endpoint that requires token authentication
@app.get("/secure-data")
async def get_secure_data(current_user: UserInDB = Depends(get_current_user)):
    return {"msg": f"Hello, {current_user.username}. You have access to secure data!"}


# Public route (no authentication required)
@app.get("/public")
async def public_route():
    return {"msg": "This is a public route!"}
