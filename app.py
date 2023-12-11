import logging
import requests
import time
import json
import os

key = os.environ['IONOS_KEY']
zone_id = os.environ['IONOS_ZONE_ID']
record_id = os.environ['IONOS_RECORD_ID']

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

previous_ip = "No IP"

def get_public_ip():
    try:

        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:

            public_ip = response.json()['origin']
            return public_ip
        else:
            logging.error(
                f"Failed to get public IP. Status code: {response.status_code}\n{response.text}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")



while True:
    public_ip_address = get_public_ip()
    
    if public_ip_address:
        logging.info(f"Your public IP address is: {public_ip_address}")
        if previous_ip != public_ip_address:
            logging.info(f"Your public IP has changed: {previous_ip} -> {public_ip_address}")
            previous_ip = public_ip_address
            url = f"https://api.hosting.ionos.com/dns/v1/zones/{zone_id}/records/{record_id}"

            data = {
                    'disabled': False,
                    'content': public_ip_address,
                    'ttl': 3600,
                    'prio': 0
                }
            logging.info(
                f"Performing request to {url} with following data:\n{json.dumps(data, indent=4)}")
            
            response = requests.put(
                url, 
                headers={
                    'accept': 'application/json',
                    'X-API-Key': key,
                    'Content-Type': 'application/json'
                }, json=data)
            
            msg = f"Response code {response.status_code}:\n{response.text}"
            if response.status_code == 200:
                logging.info(msg)
            else:
                logging.error(msg)


    else:
        logging.error("Failed to retrieve public IP address.")
    
    time.sleep(60 * 60) 
