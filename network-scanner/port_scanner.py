#!/usr/bin/python3
from scapy.all import *
import sys
conf.verb = 0

#####################################
# Usprawnienia:
#  - Mozliwosc spoofowania MAC adresu
#  - Mozliwosc spoofowania adresu IP
#  - Mozliwosc zmiany zrodlowego portu TCP
#  sr(Ether(src= ypur MAC address)(IP(dst=host["ip"], src= your IP address)/TCP(dport=nmap_top1000_int, src= ...), timeout=1)
#####################################

def load_ports_from_file(filename):
    """Funkcja ładuje z pliku listę portów"""
    ports_file = open("./nmap-top1000.txt")
    ports = ports_file.read().split(",")
    return [int(port) for port in ports]

def is_ping_reply(ping):
    """Sprawdza czy dana odpowiedź ICMP ma typ echo (ping) reply (czyli wartość liczbową 0)"""
    return ping[1][ICMP].type == 0

def is_tcp_synack(packet):
    """Sprawdza czy odpowiedź TCP ma flagę `SA` (synack), co oznacza że udało nam się pomyślnie nawiązać połączenie"""
    return packet[1][TCP].flags == "SA"

if len(sys.argv) != 2:
    print("Skrypt przyjmuje dokladnie dwa argumenty")
    print(f"python3 {sys.argv[0]} <adres sieci lub hosta>")

target = sys.argv[1]

print("[+] Stage: Host discovery")
# Wysłanie pakietów ICMP do wskazanego celu i odebranie wszystkich odpowiedzi
pings, unans = sr(IP(dst=target)/ICMP(), timeout=2)

hosts = []
# Pętla ma za zadanie sprawdzić czy dany ping jest odpowiedzią echo (ping) reply
# Jeżeli jest to host zostaje dodany do listy odkrytych hostów
for ping in pings:
    if is_ping_reply(ping) == False:
        continue
    hosts.append({
        "ip": ping[0].dst,
        "services": []
    })

print("[+] Stage: Service discovery")
nmap_top1000_int = load_ports_from_file("./nmap-top1000.txt")

# Pętla ma za zadanie wysłać do każdego odkrytego hosta 1000 pakietów TCP, na 1000 najbardziej popularnych hostów
for host in hosts:
    tcp_results, unans = sr(IP(dst=host["ip"])/TCP(dport=nmap_top1000_int), timeout=1)
    print(f'Host: {host["ip"]}')
    # Sprawdzenie, które połączenia zostały nawiązane i zapisanie wyników
    for tcp_conn in tcp_results:
        if is_tcp_synack(tcp_conn) == False:
            continue
        host["services"].append(tcp_conn[0][TCP].dport)
        print(f"\t- Open port: {tcp_conn[0][TCP].dport}")
