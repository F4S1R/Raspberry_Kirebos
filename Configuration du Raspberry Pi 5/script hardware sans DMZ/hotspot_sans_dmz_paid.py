
# Script Python : Hotspot Sécurisé sans DMZ avec logiciels payants intégrés

# Objectif : Ce script configure un hotspot WiFi sécurisé sur un Raspberry Pi ou un PC Windows avec des solutions payantes
# pour améliorer la sécurité, incluant VPN et firewall avancé.

import os

# 1. Mise à jour du système
def update_system():
    os.system("sudo apt update && sudo apt upgrade -y")

# 2. Installation des logiciels nécessaires (hostapd, dnsmasq, iptables, fail2ban, arpwatch) pour Linux
# ou alternatives payantes pour Windows
def install_packages_linux():
    os.system("sudo apt install hostapd dnsmasq bluez iptables fail2ban arpwatch -y")

# 3. Option payante (Windows) : Connectify pour transformer un PC en point d'accès WiFi sécurisé
# Connectify est une solution payante qui peut être utilisée à la place de hostapd sous Windows.
# URL : https://www.connectify.me
def setup_connectify_windows():
    print("Utiliser Connectify pour configurer un point d'accès WiFi sécurisé (payant).")
    # Connectify nécessite une installation manuelle sur Windows.

# 4. Installation et configuration de VPN payant : ExpressVPN
# ExpressVPN est un VPN payant qui peut être installé pour sécuriser toutes les connexions réseau.
# URL : https://www.expressvpn.com
def setup_vpn():
    print("Installer et configurer ExpressVPN pour une sécurité renforcée (payant).")
    # ExpressVPN nécessite une installation manuelle
    # Exemple : sur Linux -> sudo apt install expressvpn

# 5. Bannissement des adresses IP et MAC (iptables pour Linux)
def ban_ip_mac(ip_address, mac_address):
    os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")  # Bloquer IP
    os.system(f"sudo iptables -A INPUT -m mac --mac-source {mac_address} -j DROP")  # Bloquer MAC

# 6. Sécurisation avancée avec un Pare-feu (Norton Security pour Windows, iptables pour Linux)
# Norton Security est un pare-feu payant recommandé pour les utilisateurs Windows
# URL : https://us.norton.com/internetsecurity
def setup_firewall_windows():
    print("Utiliser Norton Security (payant) pour configurer un pare-feu avancé sous Windows.")
    # Installation de Norton Security requise via https://us.norton.com/internetsecurity

# Sécurisation avec iptables (pare-feu gratuit pour Linux)
def configure_firewall_linux():
    os.system("sudo iptables -F")
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")  # SSH
    os.system("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")  # HTTP
    os.system("sudo sh -c 'iptables-save > /etc/iptables/rules.v4'")

if __name__ == "__main__":
    # Exemple d'utilisation sous Linux
    update_system()
    install_packages_linux()
    setup_vpn()
    configure_firewall_linux()

    # Exemple d'utilisation sous Windows
    setup_connectify_windows()
    setup_firewall_windows()

    # Exemple de bannissement d'une IP et d'une MAC
    ban_ip_mac("192.168.50.200", "XX:XX:XX:XX:XX:XX")
