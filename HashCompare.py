import sys 
import hashlib 
import argparse

def hashfile(file): 
   
    BUF_SIZE = 65536 
    
    sha256 = hashlib.sha256() 
    
    with open(file, 'rb') as f:   
        while True:    
        data = f.read(BUF_SIZE) 
            if not data: 
                break        
            
            sha256.update(data)
    
    return sha256.hexdigest() 
  
f1_hash = hashfile(sys.argv[1]) 
f2_hash = hashfile(sys.argv[2]) 
parser = argparse.ArgumentParse()
parser.add_argument("-h", dest="param3", help="parametro3")

   
if f1_hash == f2_hash: 
    print("Ambos archivos tienen el mismo hash") 
    print(f"Hash: {f1_hash}") 
  
else: 
    print("Los archivos son diferentes ") 
    print(f"Hash del arhivo numero 1: {f1_hash}") 
    print(f"Hash del arhivo numero 2: {f2_hash}") 