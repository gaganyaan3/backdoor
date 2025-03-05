import requests
from requests import get
import socket
import argparse
parser = argparse.ArgumentParser(description='host port parameters')

parser.add_argument('--host', type=str,
                    help='host in text')
parser.add_argument('--port', type=int,
                    help='port in text')
args = parser.parse_args()
host = args.host
port = args.port

ip1 = requests.get('https://checkip.amazonaws.com').text.strip()
ip2 = get('https://api.ipify.org').content.decode('utf8')
print('checkip.amazonaws.com public IP address : {}'.format(ip1))
print('api.ipify.org         public IP address : {}'.format(ip2))

def send_data(host, port, ip1, ip2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(ip1.encode())
    s.sendall("\n".encode())
    s.sendall(ip2.encode())
    s.close()

send_data(host, port, ip1, ip2)

#python3 get_ip.py --host localhost --port 8888