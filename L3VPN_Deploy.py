import json

#### This code is under development - UNFINISHED

def main():
    """
    Main method to start this L3VPN deployment tool.
    """

    print("######################################################")
    print("####                                              ####")
    print("####  NSO L3VPN Deployment Tool                   ####")
    print("####                                              ####")
    print("####  Developer: Joel Fernandez, Ajay Doshi       ####")
    print("####  Email: joelfern@cisco.com                   ####")
    print("####                                              ####")
    print("######################################################")
    print()
    print("This tool uses the nourthbound NSO API to deploy L3VPNs")
    print()
    vpnName = input("VPN Name: ")
    routeDistinguisher = input("Route Distinguiser: ")
    print()
    print("VPN Source Config")
    sourceID = input("ID: ")
    sourceCeDevice = input("CE Device: ")
    sourceCeInterface = input("CE Interface: ")
    sourceNetwork = input("Network Address: ")
    sourceBandwidth = input("Bandwidth: ")
    sourceAsNumber = input("AS Number: ")
    print()
    print("VPN Destination Config")
    destinationID = input("ID: ")
    destinationCeDevice = input("CE Device: ")
    destinationCeInterface = input("CE Interface: ")
    destinationNetwork = input("Network Address: ")
    destinationBandwidth = input("Bandwidth: ")
    destinationAsNumber = input("AS Number: ")

data = {

    'name' : vpnName,
    'route-distinguisher' : routeDistinguisher,
    'id' : sourceID,
    'ce-device': sourceCeDevice,
    'ce-interface' : sourceCeInterface,
    'ip-network' : sourceNetwork,
    'bandwidth' : sourceBandwidth,
    'as-number' : sourceAsNumber

    'id': destinationID,
    'ce-device': destinationCeDevice,
    'ce-interface': destinationCeInterface,
    'ip-network': destinationNetwork,
    'bandwidth': destinationBandwidth,
    'as-number': destinationAsNumber
}

json_str = json.dumps(data)

if __name__ == "__main__":
    main()
