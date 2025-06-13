# backdoor
helpful backdoor

### 1. Get public ip of your local home network to other server
```
0 */1 * * * curl ifconfig.me  >/dev/tcp/server_ip/8888

0 */1 * * * python3 get_ip.py --host localhost --port 8888
```

### 2. Check internet status with custom systemd service
```
root@lp-arm-2:/etc/systemd/system# cat internet_check.service 
[Unit]
Description=internet_check
Documentation=internet_check
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
Restart=on-failure

ExecStart=/opt/internet_check.sh

[Install]
WantedBy=multi-user.target

```