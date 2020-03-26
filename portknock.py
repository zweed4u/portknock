#!/usr/bin/python3
import socket
import subprocess
import sys
from datetime import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("ip", help="ip of the machine to port scan", type=str)
args = parser.parse_args()

min_port = 1
max_port = 65536
remote_server_ip = args.ip
print(remote_server_ip)


# Check what time the scan started
t1 = datetime.now()
try:
    for port in range(min_port, max_port):
        print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_server_ip, port))
        if result == 0:
            print(f"Port {port}: 	 Open")
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

print(f"Scanning for {remote_server_ip} Completed in: {datetime.now() - t1}")
