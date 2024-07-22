import random
import string
def password_generator(length):
   C=string.ascii_letters + string.digits + string.punctuation
   P="".join(random.choice(C) for i in range(length))
   return P
password=int(input("enter the input:"))
print(password_generator(password))