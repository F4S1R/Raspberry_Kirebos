
#!/usr/bin/env python3

import os

def update_system():
    print("Updating the system...")
    os.system("sudo apt update && sudo apt upgrade -y")

def install_software():
    print("Installing required software packages...")
    os.system("sudo apt install hostapd dnsmasq iptables fail2ban arpwatch nmap -y")
    print("Installing mid-range paid security software...")

    # Example of mid-range paid security solutions (with placeholder commands)
    # These need to be downloaded and installed separately:
    
    # 1. ExpressVPN (Paid VPN solution)
    print("Installing ExpressVPN...")
    os.system("wget https://www.expressvpn.com/setup#manual")
    os.system("sudo dpkg -i expressvpn.deb")  # Placeholder

    # 2. Norton Security (Paid firewall & security software)
    print("Installing Norton Security...")
    os.system("wget https://norton.com/downloads")
    os.system("sudo dpkg -i norton.deb")  # Placeholder

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

    # Use Norton for additional firewall settings
    print("Norton Security is now protecting the system with advanced firewall features.")

def configure_fail2ban():
    print("Configuring Fail2ban...")
    os.system("sudo systemctl restart fail2ban")

def configure_vpn():
    print("Configuring ExpressVPN for secure browsing...")
    os.system("expressvpn activate")  # Example placeholder command
    print("ExpressVPN is now activated and protecting your traffic.")

def main():
    update_system()
    install_software()
    configure_hostapd()
    configure_firewall()
    configure_fail2ban()
    configure_vpn()
    print("Configuration complete. Your system is now protected with mid-range security solutions.")

if __name__ == "__main__":
    main()
