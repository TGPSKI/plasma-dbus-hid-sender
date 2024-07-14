"""Auto-generated DBus bindings

Generated by jeepney version 0.8.0

Object path: /VirtualDesktopManager
Bus name   : org.kde.KWin
"""

from jeepney.wrappers import MessageGenerator, new_method_call


class VirtualDesktopManager(MessageGenerator):
    interface = 'org.kde.KWin.VirtualDesktopManager'

    def __init__(self, object_path='/VirtualDesktopManager',
                 bus_name='org.kde.KWin'):
        super().__init__(object_path=object_path, bus_name=bus_name)

    def createDesktop(self, position, name):
        return new_method_call(self, 'createDesktop', 'us',
                               (position, name))

    def setDesktopName(self, id, name):
        return new_method_call(self, 'setDesktopName', 'ss',
                               (id, name))

    def removeDesktop(self, id):
        return new_method_call(self, 'removeDesktop', 's',
                               (id,))