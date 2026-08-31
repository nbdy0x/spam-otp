#!/usr/bin/env python3
# main.py - Spammer OTP WhatsApp (FREE VERSION)

import sys
import time
import platform
from datetime import datetime
from colorama import Fore, Style

from license import (
    clear_screen, log_info, log_success, log_warning, log_error, log_input, log_header,
    check_license, get_device_id, get_active_apis,
    VERSION, TOOLS_NAME, BANNER
)

def get_formatted_datetime():
    now = datetime.now()
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    day_name = days[now.weekday()]
    day = now.day
    month = months[now.month - 1]
    year = now.year
    return f"{day_name}, {day} {month} {year}"

def get_device_name():
    try:
        return platform.node()
    except:
        return "Unknown Device"

def show_menu():
    print(f"{Fore.CYAN}Menu Utama{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} Single Round")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} Infinite Loop")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} Keluar")
    print()

def show_thread_menu():
    clear_screen()
    log_header()
    print(f"{Fore.CYAN}Pilih Jumlah Thread (default 1){Style.RESET_ALL}")
    print()
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} 1 Thread (slow)")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} 2 Thread")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} 3 Thread")
    print(f"  {Fore.GREEN}[4]{Style.RESET_ALL} 4 Thread")
    print(f"  {Fore.GREEN}[5]{Style.RESET_ALL} 5 Thread (recommended)")
    print(f"  {Fore.GREEN}[6]{Style.RESET_ALL} 6 Thread")
    print(f"  {Fore.GREEN}[7]{Style.RESET_ALL} 7 Thread")
    print(f"  {Fore.GREEN}[8]{Style.RESET_ALL} 8 Thread")
    print(f"  {Fore.GREEN}[9]{Style.RESET_ALL} 9 Thread")
    print(f"  {Fore.GREEN}[10]{Style.RESET_ALL} 10 Thread (fast)")
    print()
    return log_input("Pilih thread (1-10, enter untuk default 1): ").strip()

def main():
    status, quota, device_id = check_license()

    while True:
        clear_screen()
        log_header()
        print(f"{Fore.CYAN}{get_formatted_datetime()} | {Fore.WHITE}{get_device_name()}{Style.RESET_ALL}")
        print()
        total_apis = get_active_apis()
        print(f"{Fore.CYAN}Available APIs : {Fore.GREEN}{total_apis}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}FREE VERSION - Full Access{Style.RESET_ALL}")
        print()
        show_menu()

        choice = log_input("Pilih menu (1/2/3): ").strip()

        if choice == "1":
            thread_choice = show_thread_menu()
            try:
                threads = int(thread_choice) if thread_choice.strip() else 1
                if threads < 1: threads = 1
                elif threads > 10: threads = 10
            except:
                threads = 1
            from main_engine import run_single_round
            run_single_round(threads=threads)
            log_info("Tekan Enter untuk kembali ke menu...")
            input()

        elif choice == "2":
            from main_engine import run_infinite_loop
            run_infinite_loop()
            log_info("Tekan Enter untuk kembali ke menu...")
            input()

        elif choice == "3":
            log_info("Keluar...")
            sys.exit(0)

        else:
            log_warning("Pilihan tidak valid. Tekan Enter untuk kembali...")
            input()

if __name__ == "__main__":
    main()
