import random
from werkzeug.security import generate_password_hash


minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = minus.upper()
numeros ="1234567890"
simbolos="@()-_*'¡?¿!<>#$%=;."

base = minus+mayus+numeros+simbolos
long = 15 


for _ in range(10):
  muestra = random.sample(base,long)
  password = "".join(muestra)
  password_encriptado = generate_password_hash(password)
  print("{} => {}".format(password,password_encriptado)) 

