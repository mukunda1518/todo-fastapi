import bcrypt

def get_password_hashed(password: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Verify the password against the hashed version
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
