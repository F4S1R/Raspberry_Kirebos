
#!/usr/bin/env python3

import os

def update_system():
    print("Mise à jour du système...")
    os.system("sudo apt update && sudo apt upgrade -y")

def install_software():
    print("Installation des paquets logiciels requis...")
    os.system("sudo apt install hostapd dnsmasq iptables fail2ban arpwatch nmap -y")

def configure_hostapd():
    print("Configuration de Hostapd pour le point d'accès WiFi...")
    with open('/etc/hostapd/hostapd.conf', 'w') as hostapd_conf:
        hostapd_conf.write('''
interface=wlan0
driver=nl80211
ssid=HotspotSecurise
hw_mode=g
channel=7
wpa=2
wpa_passphrase=VotreMotDePasseSecurise
        ''')
    os.system("sudo systemctl restart hostapd")

def configure_firewall():
    print("Configuration du pare-feu...")
    os.system("sudo iptables -F")
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")  # SSH
    os.system("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")  # HTTP

def configure_fail2ban():
    print("Configuration de Fail2ban...")
    os.system("sudo systemctl restart fail2ban")

def main():
    update_system()
    install_software()
    configure_hostapd()
    configure_firewall()
    configure_fail2ban()
    print("Configuration complète. Votre système est sécurisé avec des solutions open source.")

if __name__ == "__main__":
    main()
