from urllib import request
from passlib.context import CryptContext



pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    @staticmethod
    def bcrypt(password):
        hased_password = pwd_cxt.hash(password)
        return hased_password
    
    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
    

# Secret key to encode/decode tokens
