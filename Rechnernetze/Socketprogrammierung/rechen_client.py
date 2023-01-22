import socket
import sys
import time
import struct

Server_IP = '127.0.0.1'
Server_PORT = 50000

# 4bytes, 1byte, (4bytes,4bytes,...)
# format chars: I, B, (i,i,i)

sum = 'Summeee'
produkt = 'Produkt'

ID = struct.pack('I', 1)
OPERATION = sum.encode('utf-8')
COUNT = struct.pack('B', 3)
NUMBERS = struct.pack('iii', 1, 2, 3)

data = ID+OPERATION+COUNT+NUMBERS

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

try:
    sock.connect((Server_IP, Server_PORT))
except socket.error:
    print('unable to connect')
    sys.exit()

sock.send(data)


result = sock.recv(1024)
res = struct.unpack('i', result)
print('DAS ERGEBNIS IST: ', res)

sock.close()
