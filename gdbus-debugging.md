To troubleshoot why you're not receiving expected signals from org.kde.KWin using dbus-monitor, you can try the following approaches:

Broaden the dbus-monitor Filter: Temporarily remove specific filters to see if you can capture any signals at all. This can help determine if the issue is with the specific signal or more general.

This command will show all messages on the session bus, which can be quite verbose, but it's useful to confirm that dbus-monitor is working and that signals are being sent on the session bus.

Check D-Bus Policy: Ensure that your user has the necessary permissions to listen to the D-Bus signals you're interested in. D-Bus security policies can restrict access to certain signals.

Use gdbus to Monitor Signals: gdbus is another tool that can be used to monitor D-Bus messages. It's part of the GNOME project but can be used for KDE signals as well.

This command monitors signals from the org.kde.KWin service at the /KWin path on the session bus.

Verify the Signal Exists: Ensure that the signal you're trying to monitor actually exists and is being emitted. You can check the KDE documentation or source code for org.kde.KWin to verify the signals.

Check for Active KDE Session: Ensure that KDE is running and that the org.kde.KWin service is active and available on the D-Bus. You can use qdbus or gdbus to list services:

or

These commands check if org.kde.KWin is listed among the active services on the session bus.

Restart D-Bus Session: In some cases, restarting your D-Bus session (or even your entire session) can resolve issues with signals not being received.

Check KDE Version: Ensure that your KDE version supports the signals you're trying to monitor. It's possible that certain signals have been added, removed, or changed in different versions of KDE.

Review KDE Settings: Some KDE signals might be configurable and only emitted under certain conditions. Review KDE settings related to the desktop and window manager to ensure that the conditions for emitting the signal are met.

By systematically going through these troubleshooting steps, you should be able to identify why you're not receiving the expected D-Bus signals from org.kde.KWin.