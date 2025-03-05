# backdoor
helpful backdoor

### 1. Get public ip of your local home network to other server
```
0 */1 * * * curl ifconfig.me  >/dev/tcp/server_ip/8888

0 */1 * * * python3 get_ip.py --host localhost --port 8888
```