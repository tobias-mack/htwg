import socket
import time
import struct
from _thread import *
import threading

My_IP = '127.0.0.1'
My_PORT = 50000
server_activity_period = 30
RESULT = 0

print_lock = threading.Lock()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((My_IP, My_PORT))
    print('Listening on Port ', My_PORT, ' for incoming TCP connections')
except socket.error as e:
    print(str(e))


t_end = time.time() + server_activity_period  # Ende der Aktivitätsperiode

sock.listen(1)
print('Listening ...')

while time.time() < t_end:
    try:
        conn, addr = sock.accept()
        print('Incoming connection accepted: ', addr)
        break
    except socket.timeout:
        print('Socket timed out listening', time.asctime())


data = conn.recv(1024)
if not data:
    conn.close()
identifier = struct.unpack("I", data[:4])
operation = data[4:11].decode('utf-8')
count = struct.unpack("B", data[11:12])

unpacker = ''
countTo = 12+count[0]*4
for x in range(count[0]):
    unpacker += 'i'

numbers = struct.unpack(unpacker, data[12:countTo])


if operation == 'Summeee':
    for x in numbers:
        RESULT += x
if operation == 'Produkt':
    for x in numbers:
        RESULT *= x
conn.send(struct.pack('i', RESULT))

sock.close()
if conn:
    conn.close()
    

