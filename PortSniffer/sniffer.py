import socket
import progressbar
import pyfiglet
import colorama
from colorama import Fore, Style

# Generate ASCII art of a python
ascii_art = pyfiglet.figlet_format("Python Port Scanner")
print(Fore.YELLOW + ascii_art)

def scan_ports(ip):
    open_ports = []
    total_ports = 65535
    bar = progressbar.ProgressBar(maxval=total_ports, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for port in range(1, total_ports+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
        bar.update(port)
    bar.finish()
    print(Fore.GREEN + "Open ports:")
    for port in open_ports:
        print(Fore.CYAN + f"Port {port} is open!" + Style.RESET_ALL)

ip = input("Enter an IP address: ")
scan_ports(ip)