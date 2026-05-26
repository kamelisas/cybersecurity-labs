import socket
import argparse
import threading
from datetime import datetime

parser = argparse.ArgumentParser(description="Threaded Python Port Scanner")

parser.add_argument("--target", required=True, help="Target IP address")
parser.add_argument("--start-port", type=int, default=1, help="Starting port")
parser.add_argument("--end-port", type=int, default=1024, help="Ending port")

args = parser.parse_args()

target = args.target
start_port = args.start_port
end_port = args.end_port

print(f"\nStarting scan on {target}")
print(f"Scanning ports {start_port}-{end_port}")
print(f"Scan started at: {datetime.now()}\n")

open_ports = []

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    1521: "Oracle Database",
   1883: "MQTT",
   3306: "MySQL",
}


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"[+] Port {port} OPEN ({service})")
            open_ports.append((port, service))

        sock.close()

    except:
        pass


threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nScan finished.")

if open_ports:
    print("\nOpen ports found:")
    for port, service in open_ports:
        print(f"- {port}: {service}")
else:
    print("\nNo open ports found.")