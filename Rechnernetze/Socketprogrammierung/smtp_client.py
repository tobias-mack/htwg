import socket
import sys
import time

Server_IP = '141.37.11.129'  # IP von asmtp.htwg-konstanz.de
Server_PORT = 587

LOGIN = 'HELO rnetin\r\n'
MAIL_FROM = 'MAIL FROM:<fake@mail.de>\r\n'
REC_MAIL = 'RCPT TO:<to631mac@htwg-konstanz.de>\r\n'
DATA = 'DATA\r\n'
MESSAGE = 'Hi das ist die Mail des SMTP Clients.\r\n.\r\n'
QUIT = 'QUIT\r\n'

data = (LOGIN, MAIL_FROM, REC_MAIL, DATA, MESSAGE, QUIT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

try:
    sock.connect((Server_IP, Server_PORT))
except socket.error:
    print('unable to connect')
    sys.exit()

# sock.send(MESSAGE.encode('utf-8'))
for i in data:
    sock.send(i.encode('utf-8'))
    try:
        msg = sock.recv(1024).decode('utf-8')
        print('msg received ', msg)
    except socket.timeout:
        print('socket timed out at', time.asctime())

sock.close()
