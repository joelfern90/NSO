import requests
import sys

host = '198.18.134.28:8080'
user = 'admin'
password = 'admin'

def send_api_request():

        # Retrieving config data from RESTCONF.

        url = 'http://' + host + '/api/running/topology'

        # RESTCONF media types for REST API headers
        headers = {'Content-Type': 'application/vnd.yang.data+json',
                   'Accept': 'application/vnd.yang.data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(user, password),
                                headers=headers, verify=False)

        # return the json as text
        return response.text

def main():

    # Simple main method calling our function.

    devices = send_api_request()

    # Prints out JSON Response

    print(devices)

if __name__ == '__main__':
    sys.exit(main())