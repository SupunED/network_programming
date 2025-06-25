import socket

def check_port(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        print(f"Port {port} on {host} is open.")

    except:
        print(f"Port {port} on {host} is closed.")


check_port("www.google.com", 80)
check_port("www.google.com", 443)
check_port("www.google.com", 20)