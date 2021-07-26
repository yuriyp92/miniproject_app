import socket

class P4cox:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( ("0.0.0.0", 80) )
        self.sock.listen(5)
        self.vistas = {}

    def run(self):
        while True:
            print("esperando conexion...")
            conn, addr = self.sock.accept()
            print(addr)
            request = conn.recv(1024)
            request = request.decode()
            #print(request)
            trozos = request.split(' ')
            ruta = trozos[1]
            cb = self.vistas.get(ruta, None)
            if cb is None:
                #devolver error
                conn.send('HTTP/1.1 404 Not Found\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(self.from_template("index.html"))
                conn.close()
                continue
            plantilla = cb(None)
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(self.from_template("index.html"))
            conn.close()
    def add_view(self, ruta, callback):
        pass

    def from_template(self, plantilla):
        with open(plantilla, 'r') as f:
            return f.read()