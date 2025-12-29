import socket

BLUEKEEP = {
    "id": "CVE-2019-0708",
    "name": "BlueKeep (RDP)",
    "test": lambda target: test_bluekeep(target)
}

def test_bluekeep(target):
    # naive check: try RDP TCP 3389 connection
    host = target.replace("http://", "").replace("https://", "")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((host, 3389))
        sock.close()
        return "[!] RDP port 3389 open — BlueKeep may be possible"
    except Exception:
        return "[+] RDP not accessible (port 3389 closed)"
