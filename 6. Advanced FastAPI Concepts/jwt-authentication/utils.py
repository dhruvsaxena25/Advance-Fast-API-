from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
 
# The DB stores the HASH, never the plain password.
# You log in with the password "secret123".
fake_user_db = {
    'jhondoe': {
        'username': 'jhondoe',
        'hashed_password': pwd_context.hash('secret123'),
    }
}
 
 
def get_user(username: str):
    """Look a user up by username. Returns the dict or None."""
    return fake_user_db.get(username)
 
 
def verify_password(plain_password, hashed_password):
    """Re-hash the typed password and compare to the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)