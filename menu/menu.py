import gi

gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GtkLayerShell


class Menu:
    def __init__(self, application):
        self.window = Gtk.Window(application=application)
        self.window.set_decorated(False)
        # self.window.set_type_hint(Gdk.WindowTypeHint.DOCK)

        self.view = Gtk.MenuBar()

        # system menu
        system_menu_item = Gtk.MenuItem(label="A")
        system_menu = Gtk.Menu()
        system_menu.append(Gtk.MenuItem(label="Shut Down..."))
        system_menu_item.set_submenu(system_menu)
        self.view.add(system_menu_item)

        self.window.add(self.view)
        self.window.show_all()
        self.window.present()
