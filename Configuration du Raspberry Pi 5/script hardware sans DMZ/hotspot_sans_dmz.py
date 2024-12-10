
# Script Python : Hotspot Sécurisé sans DMZ sur Raspberry Pi

# Objectif : Ce script configure un hotspot WiFi sécurisé sur un Raspberry Pi avec gestion Bluetooth.
# Utilisation d'outils open-source comme hostapd, dnsmasq, iptables, fail2ban, et arpwatch.

import os

# 1. Mise à jour du système
def update_system():
    os.system("sudo apt update && sudo apt upgrade -y")

# 2. Installation des logiciels nécessaires (hostapd, dnsmasq, bluez, iptables, fail2ban, arpwatch)
def install_packages():
    os.system("sudo apt install hostapd dnsmasq bluez iptables fail2ban arpwatch -y")

# 3. Configuration du point d'accès WiFi sécurisé
def configure_wifi():
    # Configuration hostapd
    with open("/etc/hostapd/hostapd.conf", "w") as hostapd_conf:
        hostapd_conf.write("""
interface=wlan0
driver=nl80211
ssid=Hotspot_Securise
hw_mode=g
channel=7
wpa=2
wpa_passphrase=PasswordSecurise123
""")

    # Activation de la configuration
    os.system("sudo sed -i 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|' /etc/default/hostapd")
    os.system("sudo systemctl start hostapd")
    os.system("sudo systemctl enable hostapd")

    # Configuration DNSMASQ pour DHCP
    with open("/etc/dnsmasq.conf", "a") as dnsmasq_conf:
        dnsmasq_conf.write("""
interface=wlan0
dhcp-range=192.168.50.10,192.168.50.100,255.255.255.0,24h
""")

    os.system("sudo systemctl restart dnsmasq")

# 4. Configuration Bluetooth
def configure_bluetooth():
    os.system("sudo systemctl start bluetooth")
    os.system("sudo bluetoothctl pairable on")
    os.system("sudo bluetoothctl discoverable on")

# 5. Bannissement des adresses IP et MAC
def ban_ip_mac(ip_address, mac_address):
    os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")  # Bloquer IP
    os.system(f"sudo iptables -A INPUT -m mac --mac-source {mac_address} -j DROP")  # Bloquer MAC

# 6. Sécurisation avec iptables (pare-feu)
def configure_firewall():
    os.system("sudo iptables -F")
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")  # SSH
    os.system("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")  # HTTP
    os.system("sudo sh -c 'iptables-save > /etc/iptables/rules.v4'")

# 7. Surveillance et bannissement automatique avec Fail2Ban et Arpwatch
def configure_fail2ban():
    os.system("sudo systemctl start fail2ban")
    os.system("sudo systemctl enable fail2ban")

def configure_arpwatch():
    os.system("sudo systemctl start arpwatch")
    os.system("sudo systemctl enable arpwatch")

if __name__ == "__main__":
    # Appel des fonctions de configuration
    update_system()
    install_packages()
    configure_wifi()
    configure_bluetooth()
    configure_firewall()
    configure_fail2ban()
    configure_arpwatch()

    # Exemple de bannissement d'une IP et d'une MAC
    ban_ip_mac("192.168.50.200", "XX:XX:XX:XX:XX:XX")
