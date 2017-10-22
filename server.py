import socket
from threading import Thread 
import webbrowser

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host, port))
print('aa')
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            msg = self.sock.recv(1024).decode()
            self.sock.send(b'Received')
            webbrowser.open(str(msg))

s.listen(5)
while True:
  c, addr = s.accept()
  client(c, addr)
  c.close()
