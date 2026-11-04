
import os
import sys
import time
import webbrowser
import random

URL = "https://t.me/FilzoBot?start=f_2j8gqkH4XI"

# Terminal colors
CYAN = "\033[96m"
GREEN = "\033[92m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"

def slow(text, delay=0.025):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def progress():
    for i in range(101):
        filled = i // 5
        bar = "█" * filled + "░" * (20 - filled)
        print(f"\r  {CYAN}[{bar}] {i}%{RESET}",
              end="", flush=True)
        time.sleep(0.025)
    print()

os.system("cls" if os.name == "nt" else "clear")

print(CYAN + r"""
███╗   ███╗███████╗████████╗ █████╗
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
██╔████╔██║█████╗     ██║   ███████║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
""" + RESET)

print(PURPLE + "       M E T A   S E R V E R" + RESET)
print(WHITE + "        POWERED BY YOUR FATHER — ZIDDI 👑" + RESET)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

slow("\n  [BOOT] Initializing META SERVER...")
time.sleep(0.4)
slow("  [SYS] Loading core components...")
time.sleep(0.4)
slow("  [NET] Preparing Telegram connection...")
time.sleep(0.4)
slow("  [AUTH] Preparing launch link...")
time.sleep(0.4)

print("\n  [SYSTEM] Establishing connection")
progress()

print(GREEN + "\n  [SUCCESS] SYSTEM READY ✓" + RESET)
time.sleep(0.5)

slow("\n  [LAUNCH] Opening META SERVER BOT...")
webbrowser.open(URL)

print(GREEN + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       META SERVER IS ONLINE 🚀
       THANK YOU FOR CONNECTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""" + RESET)

input("\n  Press ENTER to exit...")
