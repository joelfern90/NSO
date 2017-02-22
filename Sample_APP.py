#
#   Cisco Network Services Orchestrator(NSO) Sample App
#       v.01
#
#   Joel Fernandez(joelfern@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Network Services Orchestrator API.
#
#   REQUIREMENTS:
#       Python sys library
#       NSO Wrapper_API module to access the NSO API
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

import sys
from Wrapper_API import Wrapper_API

def main():
    """
    Main method for our initializing our Wrapper API and calling functions
    """
    getWrapperAPI = Wrapper_API()
    getDevices = getWrapperAPI.getDevices()
    getTopology = getWrapperAPI.getTopology()
    getSnmpConfig = getWrapperAPI.getSnmpConfig()

    print(getDevices)
    print(getTopology)
    print(getSnmpConfig)

if __name__ == '__main__':
    sys.exit(main())