import socket
import threading
import requests


def send_address():
    threading.Timer(5.0, send_address).start()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    send_data("chip1", s.getsockname()[0])


def send_data(name, ip):
    url = 'https://chip-ip.herokuapp.com/api/ip'
    payload = '{"ip":"' + ip + '","name":"' + name + '"}'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)


send_address()
