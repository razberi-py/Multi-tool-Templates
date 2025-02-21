import os
import sys
import time
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows color support
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f'''{Fore.RED}
    ____  ___                      .__  __    ___________           .__   
    \   \/  /  ____________   ____ |__|/  |_  \__    ___/___   ____ |  |  
     \     /  /  ___/\____ \ /  _ \|  \   __\   |    | /  _ \ /  _ \|  |  
     /     \  \___ \ |  |_> >  <_> )  ||  |     |    |(  <_> |  <_> )  |__
    /___/\  \/____  >|   __/ \____/|__||__|     |____| \____/ \____/|____/
          \_/     \/ |__|                                                 
    {Style.RESET_ALL}{Fore.CYAN}═══════════════════════════════════════════════════════════════
    {Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Created By: Xspoit Team{Style.RESET_ALL}
    {Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Version: 2.0{Style.RESET_ALL}
    {Fore.CYAN}═══════════════════════════════════════════════════════════════{Style.RESET_ALL}
    '''
    print(banner)

def page1():
    menu = f'''
    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                        Page 1/4                                                        {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Network Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                                {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Port Scanner             {Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] Packet Sniffer           {Fore.WHITE}[{Fore.RED}7{Fore.WHITE}] Network Mapper           {Fore.WHITE}[{Fore.RED}10{Fore.WHITE}] ARP Spoofer             {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] DNS Enumerator           {Fore.WHITE}[{Fore.RED}5{Fore.WHITE}] Traffic Analyzer         {Fore.WHITE}[{Fore.RED}8{Fore.WHITE}] MAC Changer              {Fore.WHITE}[{Fore.RED}11{Fore.WHITE}] Protocol Scanner        {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] Network Monitor          {Fore.WHITE}[{Fore.RED}6{Fore.WHITE}] Bandwidth Tester         {Fore.WHITE}[{Fore.RED}9{Fore.WHITE}] Connection Tester        {Fore.WHITE}[{Fore.RED}12{Fore.WHITE}] IP Scanner              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Web Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                                    {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}13{Fore.WHITE}] SQLMap                  {Fore.WHITE}[{Fore.RED}16{Fore.WHITE}] Directory Scanner       {Fore.WHITE}[{Fore.RED}19{Fore.WHITE}] XSS Tester              {Fore.WHITE}[{Fore.RED}22{Fore.WHITE}] Web Crawler             {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}14{Fore.WHITE}] Cookie Manager          {Fore.WHITE}[{Fore.RED}17{Fore.WHITE}] SSL Analyzer            {Fore.WHITE}[{Fore.RED}20{Fore.WHITE}] Form Fuzzer             {Fore.WHITE}[{Fore.RED}23{Fore.WHITE}] API Tester              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}15{Fore.WHITE}] CMS Scanner             {Fore.WHITE}[{Fore.RED}18{Fore.WHITE}] WAF Detector            {Fore.WHITE}[{Fore.RED}21{Fore.WHITE}] HTTP Proxy              {Fore.WHITE}[{Fore.RED}24{Fore.WHITE}] Request Forger          {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}[{Fore.RED}N{Fore.WHITE}] Next Page    {Fore.WHITE}[{Fore.RED}P{Fore.WHITE}] Previous Page    {Fore.WHITE}[{Fore.RED}0{Fore.WHITE}] Exit                                                                         {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    '''
    print(menu)

def page2():
    menu = f'''
    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                      Page 2/4                                                          {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- OSINT Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                                  {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Sherlock                 {Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] PhoneInfoga              {Fore.WHITE}[{Fore.RED}7{Fore.WHITE}] Maltego                  {Fore.WHITE}[{Fore.RED}10{Fore.WHITE}] TheHarvester            {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] Recon-ng                 {Fore.WHITE}[{Fore.RED}5{Fore.WHITE}] Shodan Scanner           {Fore.WHITE}[{Fore.RED}8{Fore.WHITE}] OSRFramework             {Fore.WHITE}[{Fore.RED}11{Fore.WHITE}] Spiderfoot              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] Twint                    {Fore.WHITE}[{Fore.RED}6{Fore.WHITE}] EmailHarvester           {Fore.WHITE}[{Fore.RED}9{Fore.WHITE}] WhatsMyName              {Fore.WHITE}[{Fore.RED}12{Fore.WHITE}] Photon                  {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Doxing Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                                 {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}13{Fore.WHITE}] Nmap                    {Fore.WHITE}[{Fore.RED}16{Fore.WHITE}] Infoga                  {Fore.WHITE}[{Fore.RED}19{Fore.WHITE}] GHunt                   {Fore.WHITE}[{Fore.RED}22{Fore.WHITE}] Nexfil                  {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}14{Fore.WHITE}] Holehe                  {Fore.WHITE}[{Fore.RED}17{Fore.WHITE}] Maigret                 {Fore.WHITE}[{Fore.RED}20{Fore.WHITE}] Social Scan             {Fore.WHITE}[{Fore.RED}23{Fore.WHITE}] OSINT-Search            {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}15{Fore.WHITE}] DoxTracker              {Fore.WHITE}[{Fore.RED}18{Fore.WHITE}] UserRecon               {Fore.WHITE}[{Fore.RED}21{Fore.WHITE}] Profil3r                {Fore.WHITE}[{Fore.RED}24{Fore.WHITE}] Karma                   {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}[{Fore.RED}N{Fore.WHITE}] Next Page    {Fore.WHITE}[{Fore.RED}P{Fore.WHITE}] Previous Page    {Fore.WHITE}[{Fore.RED}0{Fore.WHITE}] Exit                                                                         {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    '''
    print(menu)

def page3():
    menu = f'''
    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                      Page 3/4                                                          {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Exploitation Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                           {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Metasploit               {Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] BeEF Framework           {Fore.WHITE}[{Fore.RED}7{Fore.WHITE}] Empire                  {Fore.WHITE}[{Fore.RED}10{Fore.WHITE}] Armitage                 {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] Cobalt Strike            {Fore.WHITE}[{Fore.RED}5{Fore.WHITE}] PowerSploit              {Fore.WHITE}[{Fore.RED}8{Fore.WHITE}] TheFatRat               {Fore.WHITE}[{Fore.RED}11{Fore.WHITE}] Veil                     {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] SET Toolkit              {Fore.WHITE}[{Fore.RED}6{Fore.WHITE}] Koadic                   {Fore.WHITE}[{Fore.RED}9{Fore.WHITE}] PoshC2                  {Fore.WHITE}[{Fore.RED}12{Fore.WHITE}] Pupy                     {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Forensics Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}13{Fore.WHITE}] Volatility              {Fore.WHITE}[{Fore.RED}16{Fore.WHITE}] Autopsy                 {Fore.WHITE}[{Fore.RED}19{Fore.WHITE}] Bulk Extractor         {Fore.WHITE}[{Fore.RED}22{Fore.WHITE}] Foremost                 {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}14{Fore.WHITE}] Wireshark               {Fore.WHITE}[{Fore.RED}17{Fore.WHITE}] FTK Imager              {Fore.WHITE}[{Fore.RED}20{Fore.WHITE}] Sleuth Kit             {Fore.WHITE}[{Fore.RED}23{Fore.WHITE}] Binwalk                  {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}15{Fore.WHITE}] NetworkMiner            {Fore.WHITE}[{Fore.RED}18{Fore.WHITE}] CAINE                   {Fore.WHITE}[{Fore.RED}21{Fore.WHITE}] DEFT                   {Fore.WHITE}[{Fore.RED}24{Fore.WHITE}] Scalpel                  {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}[{Fore.RED}N{Fore.WHITE}] Next Page    {Fore.WHITE}[{Fore.RED}P{Fore.WHITE}] Previous Page    {Fore.WHITE}[{Fore.RED}0{Fore.WHITE}] Exit                                                                         {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    '''
    print(menu)

def page4():
    menu = f'''
    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                      Page 4/4                                                          {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Network Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                                {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}1{Fore.WHITE}] Nmap                     {Fore.WHITE}[{Fore.RED}4{Fore.WHITE}] Wireshark                {Fore.WHITE}[{Fore.RED}7{Fore.WHITE}] Bettercap                {Fore.WHITE}[{Fore.RED}10{Fore.WHITE}] Responder               {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}2{Fore.WHITE}] Aircrack-ng              {Fore.WHITE}[{Fore.RED}5{Fore.WHITE}] Netcat                   {Fore.WHITE}[{Fore.RED}8{Fore.WHITE}] Ettercap                 {Fore.WHITE}[{Fore.RED}11{Fore.WHITE}] Kismet                  {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}3{Fore.WHITE}] Hydra                    {Fore.WHITE}[{Fore.RED}6{Fore.WHITE}] Tcpdump                  {Fore.WHITE}[{Fore.RED}9{Fore.WHITE}] Snort                    {Fore.WHITE}[{Fore.RED}12{Fore.WHITE}] Masscan                 {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                 {Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]- Web Tools -{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]                                                    {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}13{Fore.WHITE}] Burp Suite              {Fore.WHITE}[{Fore.RED}16{Fore.WHITE}] Nikto                   {Fore.WHITE}[{Fore.RED}19{Fore.WHITE}] Wfuzz                   {Fore.WHITE}[{Fore.RED}22{Fore.WHITE}] Skipfish                {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}14{Fore.WHITE}] OWASP ZAP               {Fore.WHITE}[{Fore.RED}17{Fore.WHITE}] Dirb                    {Fore.WHITE}[{Fore.RED}20{Fore.WHITE}] SQLmap                  {Fore.WHITE}[{Fore.RED}23{Fore.WHITE}] w3af                    {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}    {Fore.WHITE}[{Fore.RED}15{Fore.WHITE}] Acunetix                {Fore.WHITE}[{Fore.RED}18{Fore.WHITE}] Arachni                 {Fore.WHITE}[{Fore.RED}21{Fore.WHITE}] XSSer                   {Fore.WHITE}[{Fore.RED}24{Fore.WHITE}] Vega                    {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╟────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╣{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}[{Fore.RED}N{Fore.WHITE}] Next Page    {Fore.WHITE}[{Fore.RED}P{Fore.WHITE}] Previous Page    {Fore.WHITE}[{Fore.RED}0{Fore.WHITE}] Exit                                                                         {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    '''
    print(menu)

def main():
    current_page = 1
    pages = {1: page1, 2: page2, 3: page3, 4: page4}
    
    while True:
        clear_screen()
        print_banner()
        pages[current_page]()
        
        choice = input(f"\n{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] Enter your choice: {Style.RESET_ALL}").upper()
        
        if choice == '0':
            clear_screen()
            sys.exit()
        elif choice == 'N' and current_page < 4:
            current_page += 1
        elif choice == 'P' and current_page > 1:
            current_page -= 1

if __name__ == '__main__':
    main()
