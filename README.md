# AUTO-IP-MODIFIER

Automated IP Modification for IONOS Subdomains

## Overview

AUTO-IP-MODIFIER is a Docker-based solution designed to automatically update the IPv4 address associated with a subdomain record on IONOS. The project utilizes the public IPv4 address of the current device, retrieved via [https://httpbin.org/ip](https://httpbin.org/ip).

## Configuration

To set up AUTO-IP-MODIFIER, follow these steps:

1. Open the Dockerfile and update the environment variables with their respective values.
2. Create the desired subdomain on the IONOS website.
3. Obtain the necessary IDs either through the IONOS API (API key, zone ID, Record ID).

## Build & Run

Build the Docker image:

```bash
docker build . -t auto-ip-modifier-ionos
```

Run the Docker container:

```bash
docker run --name auto-ip-modifier-ionos-container -d auto-ip-modifier-ionos
```

Alternatively, run with environment values:

```bash
docker run --name auto-ip-modifier-ionos-container -d --env IONOS_KEY=<IONOS_KEY> --env IONOS_ZONE_ID=<IONOS_ZONE_ID> --env IONOS_RECORD_ID=<IONOS_RECORD_ID> auto-ip-modifier-ionos
```

## Print Logs

View the container logs:

```bash
docker exec -it auto-ip-modifier-ionos-container cat logs.log
```

## License

This project is released under an open license. Feel free to use, modify, and distribute it as needed.

## Author

Aurélien "Owrel" SIMON - Contact: aureliensimon.contact@gmail.com