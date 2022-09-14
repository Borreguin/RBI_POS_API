import bcrypt


def get_hashed_text(plain_text):
    return bcrypt.hashpw(plain_text.encode('utf8'), bcrypt.gensalt())


def verify_hashed_text(plain_text, hashed_text):
    return bcrypt.checkpw(plain_text, hashed_text)