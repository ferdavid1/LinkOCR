import socket
from demo import main

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '205.175.118.21'
print (host)
port = 12345

s.connect((host, port))
print('aa')
def ts(string):
   s.send(string.encode()) 
   data = s.recv(1024).decode()
   print (data)

while 2:
	print('Identifying...')
	r = main()
	ts(r)
	print("Done!")

s.close()
