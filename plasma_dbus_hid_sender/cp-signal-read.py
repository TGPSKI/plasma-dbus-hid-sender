from jeepney import DBusAddress, new_method_call
from jeepney.io.blocking import open_dbus_connection, Proxy
from jeepney.bus_messages import MatchRule, message_bus
import signal
import sys

connection = open_dbus_connection(bus='SESSION')
kde_address = DBusAddress('/KWin', bus_name='org.kde.KWin', interface='org.kde.KWin')


def signal_handler(sig, frame):
    print('Terminating the session...')
    connection.close()  # Close the D-Bus connection
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


def get_current_desktop(conn, addr):
    """Call the currentDesktop method and return the current desktop number."""
    method = 'currentDesktop'
    msg = new_method_call(addr, method)
    response = conn.send_and_get_reply(msg)
    try:
        desktop_number = int(response.body[0])
        print(f"Current desktop number: {desktop_number}")
        return desktop_number
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

match_rule = MatchRule(
    type="signal",
    interface="org.kde.KWin.VirtualDesktopManager",
    member="currentChanged",
    path="/VirtualDesktopManager",
    sender="org.kde.KWin"
)

bus_proxy = Proxy(message_bus, connection)
print("Match added?", bus_proxy.AddMatch(match_rule) == ())


# Main loop to listen for signals
while True:
    msg = connection.receive()
    if msg and msg.body:
        print("Signal received:", msg.body)
        get_current_desktop(connection, kde_address)

