from testfunc import encryptuser as en
class store:
    def __init__(self, user, hashes):
        self.user = user
        self.hashes = hashes
        pass
    
    def main(self,a,b):
        c = en.Func(a,b)
        self.user.append(a)
        self.hashes.append(str(c))