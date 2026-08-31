#!/usr/bin/env python3
# license.py - FREE VERSION (tanpa lisensi, tanpa batasan)

import os
import sys
import platform
from datetime import datetime
from colorama import Fore, Style

# ==================== VERSION ====================
VERSION = "3.1"
YEAR = "2026"
TOOLS_NAME = "Spammer OTP WhatsApp"

# ==================== BANNER ====================
BANNER = r"""

 /   _____/__________    _____   _____   ___________
 \_____  \____ \__  \  /     \ /     \_/ __ \_  __ \
 /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/
/_______  /   __(____  /__|_|  /__|_|  /\___  >__|
        \/|__|       \/      \/      \/     \/
"""

# ==================== RATE LIMIT KEYWORDS ====================
RATE_LIMIT_KEYWORDS = [
    'too many','rate limit','exceeded','try again',
    'coba lagi','otp telah dikirim','resend the code after',
    'terlalu banyak percobaan','please resend in',
    'VERIFICATION_CODE_REQUEST_LIMIT'
]

# ==================== FUNGSI ====================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_info(msg):
    print(f"{Fore.CYAN}[*]{Style.RESET_ALL} {msg}")

def log_success(msg):
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {msg}")

def log_warning(msg):
    print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} {msg}")

def log_error(msg):
    print(f"{Fore.RED}[-]{Style.RESET_ALL} {msg}")

def log_input(prompt):
    return input(f"{Fore.YELLOW}?{Style.RESET_ALL} {prompt}")

def log_header():
    clear_screen()
    print(f"{Fore.CYAN}{BANNER}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Spammer OTP WhatsApp v.{VERSION} {Fore.WHITE}©{YEAR}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}  nobody tools | nobody0x.com{Style.RESET_ALL}")
    print()

# ==================== FUNGSI LISENSI (FREE VERSION) ====================

def get_device_id():
    return "FREE_VERSION_NO_LICENSE"

def get_public_ip():
    try:
        import requests
        return requests.get('https://api.ipify.org', timeout=5).text.strip()
    except:
        return '127.0.0.1'

def get_active_apis():
    return 39

def is_admin_number(phone):
    return False

def check_license():
    clear_screen()
    log_header()
    print(f"{Fore.CYAN}Device ID      : {Fore.WHITE}FREE_VERSION{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Available APIs : {Fore.GREEN}39{Style.RESET_ALL}")
    print()
    log_success("FREE VERSION - Full access unlocked (tanpa lisensi)")
    print()
    return "premium", 999999, "FREE_VERSION_NO_LICENSE"
