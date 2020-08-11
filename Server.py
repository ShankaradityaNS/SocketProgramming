import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))  #WE can use port number greater than 1023#
s.listen(5)
while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} is established")
    clt.send(bytes("Socket Programming in Python", "utf-8"))
    clt.close()
