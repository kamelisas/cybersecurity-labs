import socket

target = input("Enter target IP: ")

print(f"\nScanning target: {target}\n")

for port in range(1, 101):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(0.2)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    s.close()

print("\nScan completed.")