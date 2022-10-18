import can

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
msg = can.Message(arbitration_id=0x01, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False) #Frame, data, extended_data? False
try:
    bus.send_periodic(msg,1)
    print("Message sent on {}".format(bus.channel_info))

    while True:
        message = bus.recv()
        print(message)

        if(message.arbitration_id == 0x0001):
            msg = can.Message(arbitration_id=0x02, data=[0, 0, 0, 0, 3, 1, 4, 1], is_extended_id=False)
            bus.send(msg)

except can.canError:
    print("Message NOT sent")