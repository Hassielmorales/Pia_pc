'''
import hashlib
import os

file = input (r"Ingresa la dirreccion/nombre del primer arhivo: ")
dfile = input (r"Ingresa la dirreccion/nombre del segundo arhivo: ")

afile = open(file, dfile,"rb")
bfile = afile.read()

Hash = hashlib.sha512(rfile)
print(Hash)
Hashed = Hash.hexdigest()

print(Hashed)
'''

import hashlib

file = input (r"Ingresa la dirreccion/nombre del primer arhivo: ")

afile = open (file, "rb")
bfile = afile.read()

Hash = hashlib.sha512(rfile)
print(Hash)
Hashed = Hash.hexdigest()

print(Hashed)

print(------------)

file = input (r"Ingresa la dirreccion/nombre del segundo arhivo: ")

cfile = open (file, "rb")
efile = afile.read()

Hash = hashlib.sha512(mfile)
print(Hash)
Hashe = Hash.hexdigest()

print(Hashe)





