from ReceiveData import store


u = []
h = []
storage = store(u, h)

a = str(input())
b = str(input())

storage.main(a,b)
print(storage.user[0])
print(storage.hashes[0])