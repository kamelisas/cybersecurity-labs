import socket
from datetime import datetime

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
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
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

target = input("Enter target IP: ")

print(f"\nStarting scan on {target}")
print(f"Scan started at: {datetime.now()}\n")

open_ports = []

for port, service in COMMON_PORTS.items():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} OPEN ({service})")
            open_ports.append((port, service))

        sock.close()

    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
        break
    except socket.error:
        print("[-] Could not connect to server.")
        break

print("\nScan finished.")

if open_ports:
    print("\nOpen ports found:")
    for port, service in open_ports:
        print(f"- {port}: {service}")
else:
    print("\nNo open common ports found.")