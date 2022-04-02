import hashlib

class HashFunction:
    @staticmethod
    def hash(str):
        password = str
        encodepassword = password.encode()

        
        hash = hashlib.sha256()
        hash.update(encodepassword)
        return hash.hexdigest()