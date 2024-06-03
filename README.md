# Multi App Compose in Docker

## Start Up

```bash
# build and run
docker compsoe up --build
# run
docker compsoe up
# run deamon mode
docker compsoe up -d
```

## Config at ./nginx/nginx_conf/default.conf

```javascript
// change your IP Address for fastapi is running 
server 192.168.1.103:8050;
// change your IP Address for express is running 
server 192.168.1.103:3000;
```
