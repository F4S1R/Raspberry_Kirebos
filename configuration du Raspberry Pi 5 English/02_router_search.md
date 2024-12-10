
# 2. Router Search

## Objective
Automatically detect available routers in the local network to avoid IP address conflicts and ensure Raspberry Pi interacts correctly with other network devices.

### Commands to install and run `nmap`:
```bash
sudo apt install nmap
nmap -sn 192.168.1.0/24  # Scan local network IP addresses
```

### Python Script:
```python
import nmap

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            print(f"Host: {host} - MAC: {nm[host]['addresses']['mac']}")
            
if __name__ == "__main__":
    scan_network()
```

### Comments
- This script detects routers and other devices connected to the network.
- Use it to determine if unauthorized routers are present in the network.

**Importance**: 4/5
