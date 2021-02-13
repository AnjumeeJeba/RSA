from __future__ import print_function
from Cryptodome.PublicKey import RSA
import time
import psutil

# generate2048 byte key
key = RSA.generate(2048)

start = time.time()  # starting time

# write private and public key to a file
private_key = key.export_key()
file_out = open("private.key", "wb")
file_out.write(private_key)
file_out.close()

time.sleep(1)  # sleeping for 1 sec to get 10 sec runtime

public_key = key.publickey().export_key()
file_out = open("public.key", "wb")
file_out.write(public_key)
file_out.close()

end = time.time()  # end time
print(f"Runtime of the program is  {end - start}")  # total time taken

print('CPU  % used:', psutil.cpu_percent())
print('physical memory  % used:', psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])
