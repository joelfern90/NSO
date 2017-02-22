# Script receives a list of devices currently configured under NSO.

import requests
import sys

host = '198.18.134.28:8080'
user = 'admin'
password = 'admin'

def send_api_request():
    """
    Sends a request to the API for retrieving data
    """
    url = 'http://' + host + '/api/running/devices'
    headers = {'Content-Type': 'application/vnd.yang.data+json',
                   'Accept': 'application/vnd.yang.data+json'}
    response = requests.get(url, auth=(user, password),
                                headers=headers, verify=False)

    return response.text

def main():
    """
    Main method for initializing the API request
    """
    devices = send_api_request()

    print(devices)

if __name__ == '__main__':
    sys.exit(main())