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