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
#       Python sys library
#       NSO Wrapper_API module to access the NSO API
#
#   WARNING:
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#
#   INFORMATION:
#       If you require any information please contact gve-programmability@cisco.com

import sys
from Wrapper_API import Wrapper_API

def main():

    # Simple main method calling our function.

    getWrapperAPI = Wrapper_API()
    getDevices = getWrapperAPI.getDevices()
    getTopology = getWrapperAPI.getTopology()
    getSnmpConfig = getWrapperAPI.getSnmpConfig()

    # Prints out JSON Response

    print(getDevices)
    print(getTopology)
    print(getSnmpConfig)

if __name__ == '__main__':
    sys.exit(main())