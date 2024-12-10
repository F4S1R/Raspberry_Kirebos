
#!/usr/bin/env python3

import os

def update_system():
    print("Updating the system...")
    os.system("sudo apt update && sudo apt upgrade -y")

def install_software():
    print("Installing required software packages...")
    os.system("sudo apt install hostapd dnsmasq iptables fail2ban arpwatch nmap -y")

def configure_hostapd():
    print("Configuring Hostapd for WiFi access point...")
    with open('/etc/hostapd/hostapd.conf', 'w') as hostapd_conf:
        hostapd_conf.write('''
interface=wlan0
driver=nl80211
ssid=SecureHotspot
hw_mode=g
channel=7
wpa=2
wpa_passphrase=YourSecurePassword
        ''')
    os.system("sudo systemctl restart hostapd")

def configure_firewall():
    print("Configuring firewall...")
    os.system("sudo iptables -F")
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")  # SSH
    os.system("sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")  # HTTP

def configure_fail2ban():
    print("Configuring Fail2ban...")
    os.system("sudo systemctl restart fail2ban")

def main():
    update_system()
    install_software()
    configure_hostapd()
    configure_firewall()
    configure_fail2ban()
    print("Configuration complete. Your system is secured with open-source solutions.")

if __name__ == "__main__":
    main()
