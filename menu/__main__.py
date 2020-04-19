import sys
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from dbus.mainloop.glib import DBusGMainLoop

from .menu import Menu


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.os.Menu", **kwargs)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-application-prefer-dark-theme", True)
        Menu(self)


if __name__ == "__main__":
    DBusGMainLoop(set_as_default=True)
    app = Application()
    app.run(sys.argv)
