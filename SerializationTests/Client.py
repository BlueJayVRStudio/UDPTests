import os
import json

import socket
import time
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t1 = time.time()

s.connect(('127.0.0.1', 1234))
# s.connect(('127.0.0.1', 5000))
response = s.recv(1024).decode()

print((time.time()-t1)*1000)
print(response)