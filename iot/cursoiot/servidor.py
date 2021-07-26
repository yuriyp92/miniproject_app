# micropython

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 7000))

while True:
    print("esperando mensaje...")
    data, addr = sock.recvfrom(256)
    print(addr)
    print(data)
    #responder
    msg = "pong"
    print("contestando con pong")
    sock.sendto(msg, addr)