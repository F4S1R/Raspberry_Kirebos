
# 3. Creating a WiFi and Bluetooth Access Point

## Objective
Set up a secure access point via WiFi and Bluetooth on Raspberry Pi, which will serve as a gateway in the network.

### Install WiFi and Bluetooth services:
```bash
sudo apt install hostapd dnsmasq bluez -y
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

### Configure `hostapd` for WiFi:
Create a file `/etc/hostapd/hostapd.conf`:
```bash
interface=wlan0
driver=nl80211
ssid=Secure_Hotspot
hw_mode=g
channel=6
wpa=2
wpa_passphrase=StrongPassword123
```

Activate the configuration:
```bash
sudo sed -i 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|' /etc/default/hostapd
```

### Bluetooth Configuration:
```bash
sudo systemctl start bluetooth
sudo bluetoothctl
pairable on
discoverable on
```

**Importance**: 5/5
