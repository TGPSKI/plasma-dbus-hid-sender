# import usb
# import struct
from pprint import pprint

# def hid_set_report(dev, report):
#     """ Implements HID SetReport via USB control transfer """
#     dev.ctrl_transfer(
#         0x21,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_OUT
#         9,     # SET_REPORT
#         0x200, # "Vendor" Descriptor Type + 0 Descriptor Index
#         0,     # USB interface № 0
#         report # the HID payload as a byte array -- e.g. from struct.pack()
#     )

# def hid_get_report(dev):
#     """ Implements HID GetReport via USB control transfer """
#     return dev.ctrl_transfer(
#         0xA1,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_IN
#         1,     # GET_REPORT
#         0x200, # "Vendor" Descriptor Type + 0 Descriptor Index
#         0,     # USB interface № 0
#         64     # max reply size
#     )

# def send_current_desktop_message(desktop_number):
#     value = f'D{desktop_number}'.encode('utf-8')
    
#     report = struct.pack('{}s'.format(len(value)), value)
#     try:
#         hid_set_report(dev, report)
#     except Exception as e:
#         raise ValueError(f'Error sending message: {e}')


# # Find the device - FIXME: support bluetooth, wireless, or wired
# dev = usb.core.find(idVendor=0x3434, idProduct=0x0800) # wired
# # dev = usb.core.find(idVendor=0x3434, idProduct=0xd030) # wireless

# if dev is None:
#     raise ValueError('Device not found')

# # Take over ownership of the HID interface 
# dev.reset()

# cfg = dev[0]
# intf = cfg[(0,0)]
# ep = intf[0]

# i = intf.bInterfaceNumber
# if dev.is_kernel_driver_active(i):
#     dev.detach_kernel_driver(i)

# # Send the message

# send_current_desktop_message(1)

# # Return ownership of interface
# dev.attach_kernel_driver(i)

import hid

a = hid.Device(0x3434, 0x0800)
value = 'D1'.ljust(32, '\x00')
a.send_feature_report(value.encode())

hid_device_interface = filter(lambda x: x['product_id'] == 2048 and x['usage'] == 97, hid.enumerate())

hid.Device()