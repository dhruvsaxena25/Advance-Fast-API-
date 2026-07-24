# This module handles JWTcreation and verification

from datetime import datetime, timedelta, timezone
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

SECRET_KEY = 'my_secret'            
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30
 
 
def create_access_token(data: dict):
    """Sign a JWT carrying `data` plus an expiry."""
    header = {'alg': ALGORITHM}
    # FIX: timedelta's first positional arg is DAYS. Name it `minutes`.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    payload = data.copy()
    payload.update({'exp': expire})
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')
 
 
def verify_token(token: str):       # FIX: was misspelled `verfiy_token`
    """Check signature + expiry, then return the username from `sub`."""
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()           # raises if expired
        username = claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Token missing subject')
        return username
    except JoseError:
        raise HTTPException(status_code=401, detail="Couldn't validate credentials")
 