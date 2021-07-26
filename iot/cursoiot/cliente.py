import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

msg = "ping"
print("enviando ping...")
sock.sendto(msg.encode(), ("192.168.1.36", 7000))

try:
    data, addr = sock.recvfrom(256)
except OSError:
    print("no llegó nada")
else:
    print(data)
    print(addr)

sock.close()