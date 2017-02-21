#
#   Cisco Network Services Orchestrator(NSO) Wrapper API
#        v.01
#
#   Joel Fernandez(joelfern@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Network Services Orchestrator API.
#
#   REQUIREMENTS:
#       Python requests library (issue the "pip install requests" command in shell or cmd)
#
#   WARNING:
#       This script is meant for educational purposes only.
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#
#   INFORMATION:
#       If you have further questions about this API and script, please contact GVE. Here are the contact details:
#           For internal Cisco gve-programmability@cisco.com
#           For Cisco partners, open a case at www.cisco.com/go/ph

import requests

host = '198.18.134.28:8080'
user = 'admin'
password = 'admin'

class Wrapper_API(object):

    def __init__(self):
        self.host = host
        self.user = user
        self.password = password

    def send_api_request(self, phrase):

        # Retrieving config data from RESTCONF.

        url = "http://" + host + "/api" + "/" + phrase

        # RESTCONF media types for REST API headers
        headers = {'Content-Type': 'application/vnd.yang.data+json',
                   'Accept': 'application/vnd.yang.data+json'}

        # this statement performs a GET on the specified url
        response = requests.get(url, auth=(user, password),
                                headers=headers, verify=False)

        # return the json as text
        return response.text

        # Returns list of Devices
    def getDevices(self):
        devicesURL = "running/devices"
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(devicesURL)
        return apiResponse

        # Returns device Topology
    def getTopology(self):
        TopologyURL = "running/topology"
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(TopologyURL)
        return apiResponse

        # Returns SNMP Config
    def getSnmpConfig(self):
        snmpConfigURL = "running/snmp"
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(snmpConfigURL)
        return apiResponse