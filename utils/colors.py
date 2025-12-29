# utils/colors.py
# Centralized terminal color handling for NOXPY

import sys

def supports_color() -> bool:
    """
    Returns True if the running environment supports ANSI colors.
    Safely disables colors for CI, pipes, or redirected output.
    """
    return sys.stdout.isatty()

if supports_color():
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"
else:
    # Graceful fallback (no ANSI escape sequences)
    RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = BOLD = DIM = RESET = ""
