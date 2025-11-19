# style.py

RESET = "\033[0m"
BOLD = "\033[1m"

# colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# box characters
BOX_TOP = "┌" + ("─" * 30) + "┐"
BOX_BOTTOM = "└" + ("─" * 30) + "┘"

import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
