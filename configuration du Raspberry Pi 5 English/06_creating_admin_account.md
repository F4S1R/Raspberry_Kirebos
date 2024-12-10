
# 6. Creating a Secure Administrator Account

## Objective
Create an administrator account for technicians with elevated privileges for hotspot management.

### Commands:
```bash
sudo adduser admin_tech  # Replace 'admin_tech' with desired username
sudo usermod -aG sudo admin_tech
```

**Importance**: 5/5
