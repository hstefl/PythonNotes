from fastapi import FastAPI, HTTPException, Depends, Query, Path, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
import jwt
import time
import uvicorn  # Added to allow running with `python script.py`

app = FastAPI(
    title="Demo RESTful API",
    description="Demonstrates REST principles, versioning, auth, rate limiting, caching, and docs",
    version="1.0.0"
)

# Setup CORS and Rate Limiting
# CORS (Cross-Origin Resource Sharing) allows frontend applications hosted on different origins
# (like http://localhost:3000) to communicate with this API. Without proper CORS headers,
# browsers will block cross-origin requests for security reasons.
# Here, we allow all origins ("*") for demonstration purposes, but in production
# it's important to specify allowed origins to prevent misuse or unauthorized access.
# Example for production: allow_origins=["https://yourfrontend.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Allowing all origins — use specific domains in production
    allow_credentials=True,  # Allow sending credentials like cookies or auth headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (e.g., Authorization, Content-Type)
)

# Rate Limiting Setup
# This uses the 'slowapi' package to throttle excessive client requests
# - Limiter is initialized with the client's remote address to identify unique users
# - The limiter is stored in app.state for global access
# - SlowAPIMiddleware processes the rate limits across all routes
#
# ⚠️ Note: Rate limiting is done in-memory and is not persistent.
# For scalable production use, consider Redis-based backends (slowapi supports them).
limiter = Limiter(key_func=get_remote_address)  # Identify clients based on IP address
app.state.limiter = limiter                     # Store limiter in app state
app.add_middleware(SlowAPIMiddleware)           # Enable middleware to enforce rate limits

# Dummy secret key for JWT
# ⚠️ This is hardcoded for demo purposes — in production use secure secrets from env vars or vaults
# and implement real authentication/authorization logic (e.g., hashed passwords, user DB)
dummy_secret = "myjwtsecret"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Pydantic Models
class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# In-memory storage
# ⚠️ This is for demonstration only. In production, use a database (e.g., PostgreSQL)
fake_users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# Generate JWT Token
# This function encodes a simple JWT payload. No user validation is performed here.
def create_token(user_id: int):
    payload = {"sub": user_id, "exp": time.time() + 3600}  # Token valid for 1 hour
    return jwt.encode(payload, dummy_secret, algorithm="HS256")

# Dependency to extract and validate the user from a JWT token
# ⚠️ Incomplete: No actual user verification against DB, just decodes token.
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, dummy_secret, algorithms=["HS256"])
        user_id = payload.get("sub")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Token endpoint to simulate login
@app.post("/token", response_model=Token)
def login():
    # ⚠️ This simulates login and always returns a token for user_id=1 without validation
    token = create_token(user_id=1)
    return {"access_token": token, "token_type": "bearer"}

# List users with pagination and rate limiting
@app.get("/users", response_model=List[User])
@limiter.limit("5/minute")
def list_users(skip: int = 0, limit: int = 10):
    # Demonstrates pagination using skip and limit query parameters
    return fake_users_db[skip : skip + limit]

# Get a specific user by ID (requires valid JWT token)
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int = Path(..., gt=0), current_user: int = Depends(get_current_user)):
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Create a new user entry
@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    new_id = max(u["id"] for u in fake_users_db) + 1
    new_user = {"id": new_id, **user.dict()}
    fake_users_db.append(new_user)
    return new_user

# Root endpoint demonstrating HATEOAS (Hypermedia As The Engine Of Application State)
@app.get("/", tags=["HATEOAS"])
def root():
    # Returns a welcome message and a list of links to other useful endpoints
    # HATEOAS helps clients discover available actions dynamically
    return {
        "message": "Welcome to the RESTful API",
        "links": [
            {"rel": "self", "href": "/"},
            {"rel": "users", "href": "/users"},
            {"rel": "token", "href": "/token"}
        ]
    }

# Error handler for rate limiting exceeded
@app.exception_handler(429)
def rate_limit_exceeded(request: Request, exc):
    return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

# Entry point for running the app with `python script.py`
if __name__ == "__main__":
    uvicorn.run("script:app", host="0.0.0.0", port=8000, reload=True)
