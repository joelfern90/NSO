# Retrieves a list of the devices in the topology and their links configured in NSO.

import requests
import sys

host = '198.18.134.28:8080'
user = 'admin'
password = 'admin'

def send_api_request():
    """
    Sends a request to the API for retrieving data
    """
    url = 'http://' + host + '/api/running/topology'
    headers = {'Content-Type': 'application/vnd.yang.data+json',
                   'Accept': 'application/vnd.yang.data+json'}
    response = requests.get(url, auth=(user, password),
                                headers=headers, verify=False)

    return response.text

def main():
    """
    Sends a request to the API for retrieving data
    """
    devices = send_api_request()

    print(devices)

if __name__ == '__main__':
    sys.exit(main())