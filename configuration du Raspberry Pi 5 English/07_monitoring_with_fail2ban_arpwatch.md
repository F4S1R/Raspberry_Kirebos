
# 7. Monitoring with Fail2Ban and arpwatch

## Objective
Monitor access attempts and automatically ban suspicious IP addresses. Monitor MAC addresses connected to the network.

### Install Fail2Ban:
```bash
sudo apt install fail2ban -y
```

### Fail2Ban configuration for SSH and HTTP:
Add these lines to `/etc/fail2ban/jail.local`:
```bash
[sshd]
enabled  = true
port     = 22
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 3
bantime  = 600

[http-auth]
enabled  = true
port     = 80
logpath  = /var/log/apache2/access.log
maxretry = 3
bantime  = 600
```

Restart Fail2Ban:
```bash
sudo systemctl restart fail2ban
```

### Install arpwatch to monitor MAC addresses:
```bash
sudo apt install arpwatch -y
sudo systemctl enable arpwatch
sudo systemctl start arpwatch
```

### Comments
- Monitors suspicious connections and bans unauthorized IP/MAC addresses.

**Importance**: 5/5
