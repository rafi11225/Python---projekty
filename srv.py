from database import insert_to_db
from database import show_db
from database import get_db
from database import init_db
import socket
import json



#Configure server
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(('localhost', 25444))
srv.listen(1)
print("Listening...")

while True:
    client_socket, addr = srv.accept()
    print(f"Connected to: {addr}")
    data = client_socket.recv(4096).decode('utf-8')
    if data:
        try:
            cookies = json.loads(data)
            for name, value in cookies.items():
                insert_to_db(name, value)
            client_socket.sendall(b'OK')
        except json.JSONDecodeError:
            print("Error...")
            client_socket.sendall(b'Error')
    client_socket.close()
    show_db()
            


