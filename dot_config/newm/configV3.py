from __future__ import annotations

import logging
import os

from key_bindings import KeyBindings
from newm.helper import BacklightManager
from newm.layout import Layout
from newm.view import View

'''

d8b   db d88888b db   d8b   db .88b  d88.         .d8b.  d888888b db   db  .d8b.    
888o  88 88'     88   I8I   88 88'YbdP`88        d8' `8b `~~88~~' 88   88 d8' `8b   
88V8o 88 88ooooo 88   I8I   88 88  88  88        88ooo88    88    88ooo88 88ooo88   
88 V8o88 88~~~~~ Y8   I8I   88 88  88  88 C8888D 88~~~88    88    88~~~88 88~~~88   
88  V888 88.     `8b d8'8b d8' 88  88  88        88   88    88    88   88 88   88   
VP   V8P Y88888P  `8b8' `8d8'  YP  YP  YP        YP   YP    YP    YP   YP YP   YP   

'''

logger = logging.getLogger(__name__)
mod = "L"  # o "A", "C", "1", "2", "3"
term = "kitty"


## helper to send notification

def notify(title: str, msg: str, icon="system-settings"):
    os.system(f"notify-send -i '{icon}' -a '{title}' '{msg}'")


# helper to execute a bunch of commands 

def execute_iter(commands: tuple[str, ...]):
    for command in commands:
        os.system(f"{command} &")


#  helper to get values of for systemd/ini like files.    "kitty_lock",

def set_value(keyval, file):
    var, val = keyval.split("=")
    return f"sed -i 's/^{var}\\=.*/{var}={val}/' {file}"


## Startup commands

def on_startup():
    INIT_SERVICE = (
        "systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "dbus-update-activation-environment 2>/dev/null \
        && dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "/usr/lib/xfce-polkit/xfce-polkit",
        "mako",
        "nm-applet --indicator",
        os.path.expanduser("~/.scripts/battery-status.sh"),
        "wl-paste --watch cliphist store",
        # "avizo-service",
        #"wlsunset -l 16.0867 -L -93.7561 -t 2500 -T 6000",
        #"mpv --no-video /home/klownie/Documents/Nintendo\ Wii\ Startup\ sound\ download\ \[jnf76C_qYho\].webm",
        "poweralertd -s",
        "exec ssh-agent nu",
        "xhost +",
    )
    execute_iter(INIT_SERVICE)


## Set preferences

def on_reconfigure():
    # gnome_schema = "org.gnome.desktop.interface"
    # gnome_peripheral = "org.gnome.desktop.peripherals"
    # gnome_preferences = "org.gnome.desktop.wm.preferences"
    # easyeffects = "com.github.wwmm.easyeffects"
    theme = "groot"
    icons = "Nordic-Folder"
    cursor = "Adwaita"
    font = "JetBrains Mono"
    gtk2 = "~/.gtkrc-2.0"

    GSETTINGS = (
        #f"gsettings set {gnome_preferences} button-layout :",
        f"gsettings set {gnome_preferences} theme {theme}",
        f"gsettings set {gnome_schema} gtk-theme {theme}",
        f"gsettings set {gnome_schema} color-scheme prefer-dark",
        f"gsettings set {gnome_schema} icon-theme {icons}",
        #f"gsettings set {gnome_schema} cursor-theme {cursor}",
        #f"gsettings set {gnome_schema} cursor-size 30",
        #f"gsettings set {gnome_schema} font-name '{font}'",
        #f"gsettings set {gnome_peripheral}.keyboard repeat-interval 30",
        #f"gsettings set {gnome_peripheral}.keyboard delay 250",
        #f"gsettings set {gnome_peripheral}.mouse natural-scroll false",
        #f"gsettings set {gnome_peripheral}.mouse speed 0.0",
        #f"gsettings set {gnome_peripheral}.mouse accel-profile 'default'",
        # f"gsettings {easyeffects} process-all-inputs true",
        # f"gsettings {easyeffects} process-all-outputs true",
    )


## Set GTK preferences

    def options_gtk(file, c=""):
        CONFIG_GTK = (
            set_value(f"gtk-theme-name={c}{theme}{c}", file),
            set_value(f"gtk-icon-theme-name={c}{icons}{c}", file),
            set_value(f"gtk-font-name={c}{font}{c}", file),
            set_value(f"gtk-cursor-theme-name={c}{cursor}{c}", file),
        )
        execute_iter(CONFIG_GTK)
    # options_gtk(gtk3)
    options_gtk(gtk2, '"')
    execute_iter(GSETTINGS)
    # gtk4
    # os.environ["GTK_THEME"] = theme
    # os.system("killall albert &")
    # os.system("albert &")


    notify("Reload", "update config success")


## Configurations for display

outputs = [
    {
        "name": "eDP-1",
        "scale": 1.0,
        "width": 1920,
        "height": 1080,
        "mHz": 60002,
        "pos_x": 3840,
        "pos_y": 0,
    },  # 2560/1600 },
    {
        "name": "HDMI-A-1",
        "scale": 1.0,
        "pos_x": 1920,
        "pos_y": 0,
    },
    {
        "name": "DP-1",
        "scale": 1.0,
        "pos_x": 0,
        "pos_y": 0,
    }
]


## Configure Pywm (backend used by newm)

pywm = {
    "enable_xwayland": True,
    # "xkb_model": "PLACEHOLDER_xkb_model",
    # "xkb_layout": "es",
    # "xkb_layout": "latam",
    "xkb_layout": "us",
    "xkb_variant": "intl",
    # "xkb_options": "caps:swapescape",
    "xcursor_theme": "Adwaita",
    "xcursor_size": 5,
    "focus_follows_mouse": True,
    # "contstrain_popups_to_toplevel": True,
    "encourage_csd": False,
    "renderer_mode": "pywm",
}


## Configure Background

background = {
    "path": os.path.expanduser("~/Pictures/sang-nguyen-asset_2.jpg"),
    "time_scale": 0.15,
    "anim": True,
}


## Configure window opening or closing

anim_time = 0.1
blend_time = 0.5
corner_radius = 0


## Floating app configuration

common_rules = {
    #"opacity": 0.8,
    "float": True,
    "float_size": (750, 750),
    "float_pos": (0.5, 0.5),
}
float_app_ids = (
    "albert",
    "pavucontrol",
    "blueman-manager",
    "app.landrop.landrop",
    "landrop",
    "xfce-polkit",
    "polkit",
    "FLOAT",
    "Bevy"
)
float_titles = (
    "Dialect",
    "kitty_floats",
    "kitty_floats_nofocus",
    "FLOAT"
    "Bevy"
)


## Blured apps 

blur_apps = (
    term, 
    "rofi",
    "kitty", 
    "tenacity",
    "kitty_lock",
     #"lock",
)


## Some special rules about viewing when certain apps are opened

def rules(view: View):

    ## default

    app_rule = None

    ## Show view info

    # os.system(
    #     f"echo '{view.app_id}, {view.title}, {view.role}, {view.pid}, {view.panel}' >> ~/.config/newm/apps"
    # )

    ## Set float common rules

    # if view.up_state.is_floating and view.app_id != "albert":
    #     app_rule = common_rules

    if view.app_id == "catapult":
        app_rule = {"float": True, "float_pos": (0.5, 0.1)}

    elif view.app_id == "io.bassi.Amberol":
        app_rule = {"opacity": 0.7, "blur": {"radius": 5, "passes": 6}}

    elif view.app_id == "app.landrop.landrop" and view.title == "Transferring":
        app_rule = {
            "float": True,
            "float_size": (600, 100),
            "float_pos": (0.5, 0.15),
        }

    elif view.app_id in float_app_ids or view.title in float_titles:
        app_rule = common_rules

    elif view.app_id in blur_apps:
        app_rule = {"blur": {"radius": 5, "passes": 6}}
    return app_rule


## Tiling configuration

view = {
    "padding": 8,
    "fullscreen_padding": 0,
    "send_fullscreen": False,
    "accept_fullscreen": False,
    "sticky_fullscreen": True,
    "floating_min_size": False,
    # "border_ws_switch": 3,
    "rules": rules,
    "debug_scaling": False,
    "ssd": {"enabled": False},
}


focus = {
    # "color": "#cba6f7",  # change color
    # "distance": 4.5,
    # "width": 4.5,
    # "animate_on_change": True,
    # "anim_time": 0.3
    "enabled": False
}


swipe_zoom = {
    "grid_m": 1,
    "grid_ovr": 0.02,
}


backlight_manager = BacklightManager(anim_time=1.0)
# # Config for keyboard light
# kbdlight_manager = BacklightManager(
#     args="--device='*::kbd_backlight'", anim_time=1.0, bar_display=wob_runner
# )


def synchronous_update() -> None:
    # kbdlight_manager.update()
    backlight_manager.update()


def key_bindings(layout: Layout):
    return KeyBindings(layout, mod, term).get()


gestures = {
    "lp_freq": 120.0,
    "lp_inertia": 0.4,
    # "c": {"enabled": False},
    # "pyevdev": {"enabled": True},
}

swipe = {"gesture_factor": 3}

panels = {
    "lock": {
        "cmd": f"{term} -e newm-panel-basic lock --title kitty_lock",
        "w": 0.7,
        "h": 0.7, 
        "corner_radius": 15,
    },
    "bar": {
        "cmd": "waybar",
        "visible_normal": False,
        "visible_fullscreen": False,
    },
}

grid = {"throw_ps": [2, 10]}


## Configuration time till lock and suspend

energy = {"idle_times": [120, 600, 1500], "idle_callback": backlight_manager.callback}
