import socket

# Dictionary for common ports
common_ports = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_ports(target, ports):
    print(f"\nScanning target: {target}\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                service = common_ports.get(port, "Unknown Service")
                print(f"[+] Port {port} ({service}) is OPEN")
            else:
                service = common_ports.get(port, "Unknown Service")
                print(f"[-] Port {port} ({service}) is CLOSED or FILTERED")
            sock.close()
        except:
            pass

if __name__ == "__main__":
    website = input("Enter website (e.g., google.com): ")
    try:
        target_ip = socket.gethostbyname(website)
    except socket.gaierror:
        print("❌ Invalid domain or DNS error.")
        exit(1)

    # Ports you want to scan
    ports_to_scan = [21, 22, 25, 53, 80, 110, 143, 443, 3306, 3389]

    scan_ports(target_ip, ports_to_scan)
