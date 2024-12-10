
# 1. System Update and Driver Installation

## Objective
Update Raspberry Pi and install necessary drivers to manage network interfaces (USB, WiFi, Bluetooth).

### Commands
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install usb-modeswitch ethtool hostapd dnsmasq iptables python3 bluetooth bluez -y
```

### Comments
- Updating is necessary to ensure compatibility with the latest versions of the packages.
- Installing Bluetooth packages via `bluez` to manage Bluetooth connections.

**Importance**: 5/5
