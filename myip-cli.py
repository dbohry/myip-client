import socket
import threading
def get_ip_address():
    threading.Timer(5.0, get_ip_address).start()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])

get_ip_address()
