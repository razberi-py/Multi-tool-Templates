#!/usr/bin/env python3
import os
import time

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"

# Advanced ASCII Art Banner (using Unicode box drawing)
print(BOLD + CYAN)
print("╔" + "═" * 70 + "╗")
print("║" + " " * 70 + "║")
print("║" + " MULTI-TOOL INTERFACE v1.0 ".center(70) + "║")
print("║" + " Advanced ASCII Display ".center(70) + "║")
print("║" + " " * 70 + "║")
print("╚" + "═" * 70 + "╝" + RESET)
print()

# Define parameters for our grid table (7 rows x 5 columns, each cell 25 characters wide)
cell_width = 25
columns = 5
rows = 7

# Fake tool names (1-35)
tools = [
    "1.  IP Grabber",    "2.  Stress Tester",  "3.  Port Scanner",      "4.  Packet Sniffer",    "5.  Subnet Calc.",
    "6.  MAC Spoofer",    "7.  Hash Cracker",   "8.  DNS Resolver",      "9.  Proxy Scraper",     "10. SQL Vuln Finder",
    "11. Rev Shell Gen",  "12. Keylogger Crtr", "13. Email Bomber",      "14. SSH Brute Force",   "15. Wifi Decrypter",
    "16. Ping Flooder",   "17. WHOIS Lookup",   "18. DDoS Simulator",    "19. RDP Cracker",       "20. Log File Analyzer",
    "21. Exploit Builder","22. XSS Detector",   "23. API Scanner",       "24. Crypto Wallet",     "25. Dir Brute Forcer",
    "26. File Hasher",    "27. Phish Page Gen", "28. ZIP Pwd Tester",    "29. Webcam Access",     "30. FTP Scanner",
    "31. URL Obfuscator", "32. Sess Hijacker",  "33. VPN Kill Switch",   "34. Tor Node Tester",   "35. Dark Web Crawler"
]

# Build table borders using Unicode box-drawing characters:
top_line    = "┌" + ("─" * cell_width)
for col in range(1, columns):
    top_line += "┬" + ("─" * cell_width)
top_line    += "┐"

mid_line    = "├" + ("─" * cell_width)
for col in range(1, columns):
    mid_line += "┼" + ("─" * cell_width)
mid_line    += "┤"

bottom_line = "└" + ("─" * cell_width)
for col in range(1, columns):
    bottom_line += "┴" + ("─" * cell_width)
bottom_line += "┘"

# Print the table with colors:
print(BOLD + YELLOW + top_line + RESET)
for r in range(rows):
    row_str = "│"
    for c in range(columns):
        index = r * columns + c
        cell = tools[index] if index < len(tools) else ""
        # Center the cell text within the fixed width
        row_str += " " + cell.center(cell_width - 1) + "│"
    print(BOLD + YELLOW + row_str + RESET)
    if r < rows - 1:
        print(BOLD + YELLOW + mid_line + RESET)
print(BOLD + YELLOW + bottom_line + RESET)
print()

# Footer instructions with color
print(BOLD + MAGENTA + "NOTE: This is a display-only interface. Functionality is disabled." + RESET)
print(BOLD + MAGENTA + "Press Ctrl+C to exit." + RESET)
time.sleep(1)
