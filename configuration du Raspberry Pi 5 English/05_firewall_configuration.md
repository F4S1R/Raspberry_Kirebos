
# 5. Firewall Configuration (iptables)

## Objective
Configure a firewall to restrict unauthorized network connections on Raspberry Pi.

### Firewall configuration commands:
```bash
sudo iptables -F
sudo iptables -P INPUT DROP
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # SSH
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # HTTP
```

Save the rules:
```bash
sudo sh -c 'iptables-save > /etc/iptables/rules.v4'
```

### Comments
- The firewall is essential to restrict unauthorized connections.
- It protects both SSH and HTTP access, while blocking all other connections by default.

**Importance**: 5/5
