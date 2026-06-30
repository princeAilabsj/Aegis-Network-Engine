import socket
import sys

# Aegis Network Engine - Core Scanner
def scan_target(target):
    print(f"[*] Initializing Aegis Audit on: {target}")
    try:
        for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            s.close()
    except KeyboardInterrupt:
        print("\n[!] Audit Aborted.")
        sys.exit()

if __name__ == "__main__":
    target = "127.0.0.1"
    scan_target(target)
