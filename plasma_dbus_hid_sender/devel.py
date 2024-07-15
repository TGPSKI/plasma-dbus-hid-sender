import usb
import struct

def hid_set_report(dev, report):
    """ Implements HID SetReport via USB control transfer """
    dev.ctrl_transfer(
        0x21,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_OUT
        9,     # SET_REPORT
        0x200, # "Vendor" Descriptor Type + 0 Descriptor Index
        0,     # USB interface № 0
        report # the HID payload as a byte array -- e.g. from struct.pack()
    )

def hid_get_report(dev):
    """ Implements HID GetReport via USB control transfer """
    return dev.ctrl_transfer(
        0xA1,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_IN
        1,     # GET_REPORT
        0x200, # "Vendor" Descriptor Type + 0 Descriptor Index
        0,     # USB interface № 0
        64     # max reply size
    )

dev = usb.core.find(idVendor=0x3434, idProduct=0x0800)

value = 1
report = struct.pack('I', value)
# Send the feature report
hid_set_report(dev, report)

# qdbus org.kde.KWin /KWin currentDesktop