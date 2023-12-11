# AUTO-IP-MODIFIER
Automatic IP change for subdomain for IONOS. This project aims to change the the IPv4 of a subdomain record of IONOS by the public IPv4 (via https://httpbin.org/ip) of the current device.

## Configuration

In the dockerfile, please change the environment variables to their corresponding values. You need to create the subdomain first on IONOS website and gather the different id through the API or run the docker run command with environments value.


## Build & run

```bash
docker build . -t auto-ip-modifier-ionos
```

```bash
docker run --name auto-ip-modifier-ionos-container -d auto-ip-modifier-ionos 
```

### Run with env values

```bash
docker run --name auto-ip-modifier-ionos-container -d --env IONOS_KEY=<IONOS_KEY> --env IONOS_ZONE_ID=<IONOS_ZONE_ID> --env IONOS_RECORD_ID=<IONOS_RECORD_ID> auto-ip-modifier-ionos 
```


### Print logs

```bash
docker exec -it auto-ip-modifier-ionos-container cat logs.log  
```


## License

Please do whatever you want with this project


## Author
@ Aurélien "Owrel" SIMON - aureliensimon.contact@gmail.com 