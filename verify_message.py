from __future__ import print_function
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
import time
import psutil
start = time.time()  # starting time
# read the public key
key = RSA.import_key(open('public.key').read())

# read the received message and the received signature
file_in = open("message.txt", "rb")
message = file_in.read()
file_in.close()

file_in = open("signature.pem", "rb")
signature = file_in.read()
file_in.close()

h2 = SHA256.new(message)

try:
    pkcs1_15.new(key).verify(h2, signature)
    print("The signature is valid. Message has not been changed. ")
except (ValueError, TypeError):
    print("The signature is not valid. This is not the original message!!!")

time.sleep(1)  # sleeping for 1 sec to get 10 sec runtime
end = time.time()  # end time
print(f"Runtime of the program is  {end - start}")  # total time taken
print('CPU  % used:', psutil.cpu_percent())
print('physical memory  % used:', psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])
