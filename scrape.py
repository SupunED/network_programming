import requests
from bs4 import BeautifulSoup
import time
import socket

iterations = 5

URL = input("Enter a valid URL in format 'https://www.example.com':\n")
try:
    ip_address = socket.gethostbyname(URL.split('://')[-1].split('/')[0])
    host_info = socket.gethostbyaddr(ip_address)
except (socket.gaierror, socket.herror) as e:
    print(f"Error resolving host: {e}")
    exit(1)

for i in range(iterations):
    time.sleep(10)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(f"Hostname: {host_info[0]}\nIP Address: {host_info[1]}\n----------------------------------------") 
    print(soup.prettify())
    print(f"\n--------------------------------------------------\n")
