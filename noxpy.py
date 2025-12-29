#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NOXPY
-----
Modular Vulnerability Detection Framework (LAB USE)
"""

import sys
import time
from utils.banner import print_banner
from vulnerabilities import registry

def prompt_target():
    print("\n[?] Enter target (URL or IP):")
    target = input("> ").strip()
    if not target.startswith(("http://", "https://")) and "." in target:
        target = "http://" + target
    return target.rstrip("/")

def main():
    print_banner()
    target = prompt_target()

    print("\n[*] Loaded vulnerability checks:")
    for v in registry.VULNERABILITIES:
        print(f"  - {v['id']} ({v['name']})")

    print("\n[*] Beginning assessment...\n")
    time.sleep(0.5)

    for vuln in registry.VULNERABILITIES:
        print(f"=== {vuln['id']} :: {vuln['name']} ===")
        try:
            result = vuln["test"](target)
            print(result)
        except Exception as e:
            print(f"[!] Error running check: {e}")
        print()

    print("[*] Assessment complete 🦊")

if __name__ == "__main__":
    main()
