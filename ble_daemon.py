import time
from losantmqtt import Device
from bluetooth.ble import DiscoveryService

# Construct device
device = Device("my-device-id", "my-app-access-key", "my-app-access-secret")

def on_command(device, command):
    print("Command received.")
    print(command["name"])
    print(command["payload"])

# Listen for commands.
device.add_event_observer("command", on_command)

# Connect to Losant.
device.connect(blocking=False)

# Send device_name once every second.
while True:
    service = DiscoveryService()
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, address: {}".format(name, address))
    device.send_state({"devices" : devices.items()})

    time.sleep(1)
