import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator
import subprocess
import signal

class NewmCmdIndicator():
    def __init__(self):
        self.app = appindicator.Indicator.new(
            "newm-cmd-indicator",
            "indicator-messages",
            appindicator.IndicatorCategory.APPLICATION_STATUS)
        self.app.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.app.set_label("Activate newm-cmd", "8.1")
        self.app.connect("activate", self.activate_newm_cmd)

    def activate_newm_cmd(self, widget, event):
        if self.app.get_label() == "Activate newm-cmd":
            self.app.set_label("Deactivate newm-cmd")
            self.process = subprocess.Popen(["newm-cmd", "inhibit-idle"])
        else:
            self.app.set_label("Activate newm-cmd")
            self.process.send_signal(signal.SIGINT)

    def main(self):
        Gtk.main()

if __name__ == "__main__":
    indicator = NewmCmdIndicator()
    indicator.main()

