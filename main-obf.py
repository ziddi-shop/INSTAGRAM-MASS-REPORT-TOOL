import os
import sys
import time
import webbrowser
from urllib.parse import quote

USERNAME = "fadingwithher"
MESSAGE = "Hello! I want to purchase Insta Mass Report Tool for $50. Please share the payment details."

URL = f"https://t.me/{USERNAME}?text={quote(MESSAGE)}"

CYAN = "\033[96m"
GREEN = "\033[92m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
RED = "\033[91m"
YELLOW = "\033[93m"
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
        print(f"\r  {CYAN}[{bar}] {i}%{RESET}", end="", flush=True)
        time.sleep(0.025)
    print()

def banner():
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
    print(WHITE + "   POWERED BY YOUR FATHER — ZIDDI 👑" + RESET)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def main():
    banner()

    slow("\n  [BOOT] Initializing META SERVER...")
    time.sleep(0.4)
    slow("  [SYS] Loading core components...")
    time.sleep(0.4)
    slow("  [NET] Preparing Telegram connection...")
    time.sleep(0.4)
    slow("  [AUTH] Checking premium access...")
    time.sleep(0.5)

    print("\n  [SYSTEM] Establishing connection")
    progress()

    print(GREEN + "\n  [SUCCESS] SYSTEM READY ✓" + RESET)
    time.sleep(0.5)

    print(PURPLE + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            PREMIUM ACCESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""" + RESET)

    print(YELLOW + "  THIS TOOL IS PAID." + RESET)
    print(WHITE + "  Price: $50 FIXED" + RESET)

    while True:
        choice = input("\n  PURCHASE ACCESS? (YES/NO): ").strip().upper()

        if choice in ("YES", "Y"):
            print(GREEN + "\n  [SUCCESS] Purchase request initiated!" + RESET)
            slow("  [LAUNCH] Opening Telegram purchase chat...")
            time.sleep(0.5)

            if webbrowser.open(URL):
                print(GREEN + "\n  [SUCCESS] Telegram chat opened ✓" + RESET)
                print(CYAN + "  [INFO] Purchase message pre-filled." + RESET)
            else:
                print(RED + "\n  [ERROR] Could not open Telegram link." + RESET)
            break

        elif choice in ("NO", "N"):
            print(RED + "\n  [DENIED] Purchase cancelled." + RESET)
            break

        else:
            print(RED + "\n  [ERROR] Invalid choice! Enter YES or NO." + RESET)

    print(GREEN + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          META SERVER
       THANK YOU FOR VISITING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""" + RESET)

    input("\n  Press ENTER to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n\n  [EXIT] Program terminated." + RESET)
        sys.exit(0)
