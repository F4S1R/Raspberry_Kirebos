
# Script Python : Hotspot Sécurisé sans DMZ avec solutions payantes

# Objectif : Ce script configure un hotspot WiFi sécurisé sur un Raspberry Pi avec gestion Bluetooth.
# Utilisation d'outils open-source et options payantes pour améliorer la sécurité.

import os

# 1. Mise à jour du système
def update_system():
    os.system("sudo apt update && sudo apt upgrade -y")

# 2. Installation des logiciels nécessaires (hostapd, dnsmasq, iptables, fail2ban, arpwatch)
# Solutions gratuites.
def install_packages():
    os.system("sudo apt install hostapd dnsmasq bluez iptables fail2ban arpwatch -y")

# 3. Option payante (Windows) : Connectify pour transformer un PC en point d'accès WiFi sécurisé
# Connectify est une solution payante qui peut être utilisée à la place de hostapd sous Windows.
# URL : https://www.connectify.me
def notify_connectify():
    print("Utiliser Connectify (payant) sur Windows pour le point d'accès WiFi sécurisé.")

# 4. Option payante : VPN ExpressVPN pour sécuriser les connexions
# ExpressVPN est une solution VPN payante recommandée pour sécuriser toutes les connexions réseau.
# URL : https://www.expressvpn.com
def setup_vpn():
    print("Installer ExpressVPN pour une sécurité supplémentaire sur les connexions réseau (option payante).")

# 5. Bannissement des adresses IP et MAC
def ban_ip_mac(ip_address, mac_address):
    os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")  # Bloquer IP
    os.system(f"sudo iptables -A INPUT -m mac --mac-source {mac_address} -j DROP")  # Bloquer MAC

# 6. Pare-feu avancé : Option payante (Norton Security, ou équivalent)
# Utiliser Norton Security ou des solutions payantes pour une protection avancée sur Windows
# URL : https://us.norton.com/internetsecurity
def notify_firewall_norton():
    print("Norton Security (payant) peut être utilisé pour renforcer la sécurité du pare-feu.")

# 7. Sécurisation avec iptables (pare-feu gratuit pour Linux)
def configure_firewall():
    os.system("sudo iptables -F")
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")  # SSH
    os.system("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")  # HTTP
    os.system("sudo sh -c 'iptables-save > /etc/iptables/rules.v4'")

if __name__ == "__main__":
    update_system()
    install_packages()
    notify_connectify()
    setup_vpn()
    configure_firewall()
    notify_firewall_norton()
    # Exemple de bannissement d'une IP et d'une MAC
    ban_ip_mac("192.168.50.200", "XX:XX:XX:XX:XX:XX")
