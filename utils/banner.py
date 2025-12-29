import random
import time
from utils.colors import GREEN, ENDC

def print_banner():
    titles = [
        "Reality is under no obligation to be convenient",
        "Trust, but verify",
        "The fox knows many things",
    ]

    foxes = [
        r"""
  /\_/\  
 ( o.o )  
  > ^ <
""",
        r"""
  /\_/\  
 ( -.- )  
  > ^ <
""",
        r"""
  /\_/\  
 ( ^.^ )  
  > ~ <
"""
    ]

    banner = f"""
{GREEN}
 ███╗   ██╗ ██████╗ ██╗  ██╗██████╗ ██╗   ██╗
 ████╗  ██║██╔═══██╗╚██╗██╔╝██╔══██╗╚██╗ ██╔╝
 ██╔██╗ ██║██║   ██║ ╚███╔╝ ██████╔╝ ╚████╔╝
 ██║╚██╗██║██║   ██║ ██╔██╗ ██╔═══╝   ╚██╔╝
 ██║ ╚████║╚██████╔╝██╔╝ ██╗██║        ██║
 ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝        ╚═╝
{ENDC}
 NOXPY — Modular Vulnerability Detection
 [{random.choice(titles)}]
{random.choice(foxes)}
"""
    print(banner)
    time.sleep(0.3)
