"""
API Key authentication to issue JWT tokens, which are then used for secured API access.

Step-by-Step Flow
1. Client Requests a JWT Token
 * The client sends an API key (X-API-KEY) to /token to obtain a JWT token.
 * The server verifies the key and returns a JWT token.

2. Client Uses JWT Token for API Requests
 * The client includes the JWT token in the Authorization header (Bearer <token>) for subsequent API calls.
 * The server validates the token before granting access to protected endpoints.
"""
import datetime
import os
from typing import List

import jwt
from anyio import get_current_task
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.params import Security, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

load_dotenv()

# Key for encoding/decoding token.
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
# What algorithm use for encoding/decoding token.
ALGORITHM = "HS256"
# How long it takes before token expires
ACCESS_TOKEN_EXPIRES_MINUTES = 3

app = FastAPI()

app_keys = {
    "app1": "app1-secret-key",
    "app2": "app1-secret-key"
}

# Define API Key Authentication.
api_key_header = APIKeyHeader(name="X-API-KEY")


def verify_api_key(api_key: str = Security(api_key_header)):
    """
    Verifies that API key provided via HTTP header is among stored
    Args:
        api_key: API key send via HTTP
    Returns:
        application name
    Exceptions
        HTTPException in case API key was not verified successfully.
    """
    for app_name, stored_key in app_keys.items():
        if api_key == stored_key:
            return app_name

    raise HTTPException(status_code=403, detail="Invalid API key")


def create_access_token(app_name: str, expires_delta: int = ACCESS_TOKEN_EXPIRES_MINUTES):
    """
    Encode application name and expiration time to create token for further communication.
    Args:
        app_name:
        expires_delta:
    Returns:
        Access token, to be used with each subsequent on API
    """
    to_encode = {"app": app_name}
    expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/token")
def generate_token(app_name: str = Depends(verify_api_key)):
    """
    Login endpoint to generate token for a valid API key
    """
    access_token = create_access_token(app_name)
    return {"access_token": access_token, "token_type": "bearer"}


# Protect endpoints with JWT Token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_app(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    return payload


# Define a Pydantic model for user data
class User(BaseModel):
    id: int
    name: str
    email: str


# In-memory database (list of users)
users_db = [User(id=1, name="John Doe", email="john@doe.com"), User(id=2, name="Joana Doe", email="joana@doe.com")]


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.get("/users", response_model=List[User])
def get_users(current_app: dict = Depends(get_current_app)):
    return users_db


@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int, current_app: dict = Depends(get_current_app)):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"User not found ")


@app.post("/users", response_model=User)
def create_user(new_user: User, current_app: dict = Depends(get_current_app)):
    for user in users_db:
        if user.id == new_user.id:
            raise HTTPException(status_code=400, detail="Users exists already")
    users_db.append(new_user)
    return new_user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
