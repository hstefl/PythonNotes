import socket

address = input("Tell me the address:")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((address, 80))
sock.send(b"GET / HTTP/1.1\r\n"
          + b"Host:" + bytes(address, 'UTF-8') + b"\r\n"
          + b"Connection: close\r\n"
          + b"\r\n")

response = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()

print(repr(response))
