import socket

ETERNALBLUE = {
    "id": "CVE-2017-0144",
    "name": "EternalBlue (SMBv1)",
    "test": lambda target: test_eternalblue(target)
}

def test_eternalblue(target):
    # naive check: try SMB TCP 445 connection
    host = target.replace("http://", "").replace("https://", "")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((host, 445))
        sock.close()
        return "[!] SMB port 445 open — EternalBlue may be possible"
    except Exception:
        return "[+] SMB not accessible (port 445 closed)"
