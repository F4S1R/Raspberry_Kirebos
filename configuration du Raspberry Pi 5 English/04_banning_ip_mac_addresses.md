
# 4. Banning IP and MAC Addresses

## Objective
Block unauthorized devices using IP and MAC addresses via iptables.

### Commands to block an IP:
```bash
sudo iptables -A INPUT -s 192.168.50.200 -j DROP
```

### Commands to block a MAC address:
```bash
sudo iptables -A INPUT -m mac --mac-source XX:XX:XX:XX:XX:XX -j DROP
```

### Python Script:
```python
import os

def block_mac(mac_address):
    os.system(f"sudo iptables -A INPUT -m mac --mac-source {mac_address} -j DROP")

block_mac('XX:XX:XX:XX:XX:XX')
```

### Comments
- Automates banning of unauthorized devices based on MAC addresses.
- Compatible for both WiFi and Bluetooth connections.

**Importance**: 5/5
