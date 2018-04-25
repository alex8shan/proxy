import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))
message = b'GET http://www.bing.com/ HTTP/1.1\r\n\r\n'
s.sendall(message)
data = s.recv(1000000)
print(data[:1000])