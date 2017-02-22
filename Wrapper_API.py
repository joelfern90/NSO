#
#   Cisco Network Services Orchestrator(NSO) Wrapper API
#       v.01
#
#   Joel Fernandez(joelfern@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Network Services Orchestrator API.
#
#   REQUIREMENTS:
#       Python requests library (issue the 'pip install requests' command in shell or cmd)
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
#test
import requests

host = '198.18.134.28:8080'
user = 'admin'
password = 'admin'

class Wrapper_API(object):
    """
    This class is uesd to interact with the NSO API
    """
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password

    def send_api_request(self, phrase):
        """
        Sends a request to the API for retrieving data.
        """
        url = 'http://' + host + '/api' + '/' + phrase
        headers = {'Content-Type': 'application/vnd.yang.data+json',
                   'Accept': 'application/vnd.yang.data+json'}
        response = requests.get(url, auth=(user, password),
                                headers=headers, verify=False)
        return response.text

    def getDevices(self):
        """
        Retreives a list of devices from the NSO API
        """
        devicesURL = 'running/devices'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(devicesURL)
        return apiResponse

    def getTopology(self):
        """
        Retrieves a list of devices and their relationships in a topology from the NSO API
        """
        TopologyURL = 'running/topology'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(TopologyURL)
        return apiResponse

    def getSnmpConfig(self):
        """
        Retries SNMP config form the NSO API
        """
        snmpConfigURL = 'running/snmp'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(snmpConfigURL)
        return apiResponse