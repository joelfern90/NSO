## Still testing how to send specific JSON payload. Maybe need to create external JSON file

import requests

url = "http://198.18.134.28:8080/api/running/vpn"
user = 'admin'
password = 'admin'
payload = "{\n  \"l3vpn:l3vpn\": {\n    \"name\": \"test\",\n    \"route-distinguisher\": 321,\n    \"endpoint\": [\n      {\n        \"id\": \"HQ\",\n        \"ce-device\": \"ce2\",\n        \"ce-interface\": \"GigabitEthernet0/1\",\n        \"ip-network\": \"11.11.1.0/24\",\n        \"bandwidth\": 900000,\n        \"as-number\": 65201\n      },\n      {\n        \"id\": \"SVT\",\n        \"ce-device\": \"ce3\",\n        \"ce-interface\": \"GigabitEthernet0/1\",\n        \"ip-network\": \"11.11.2.0/24\",\n        \"bandwidth\": 300000,\n        \"as-number\": 65202\n      }\n    ]\n  }\n}"
headers = {
    'content-type': "application/vnd.yang.data+json",
    }

response = requests.request("POST", url, data=payload, headers=headers, auth=(user, password))

print(response.text)
