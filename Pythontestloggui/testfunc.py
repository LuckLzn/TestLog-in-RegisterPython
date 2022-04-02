from hash import HashFunction as Hf
import string
class encryptuser:
    @staticmethod
    def Func(User, Pass):
        User = str(User)
        Password = str(Pass)
        hasheduser = Hf.hash(User)
        hashedpass = Hf.hash(Password)
        hashedpass = str(hashedpass)
        hasheduser = str(hasheduser)
        hash = hasheduser + hashedpass
        hash = Hf.hash(hash)
        
        return hash
      
        