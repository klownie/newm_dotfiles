import os

from newm.layout import Layout
from newm.view import View

'''

d8b   db d88888b db   d8b   db .88b  d88.   .d8888. db   db  .d88b.  d8888b. d888888b  .o88b. db    db d888888b .d8888. 
888o  88 88'     88   I8I   88 88'YbdP`88   88'  YP 88   88 .8P  Y8. 88  `8D `~~88~~' d8P  Y8 88    88 `~~88~~' 88'  YP 
88V8o 88 88ooooo 88   I8I   88 88  88  88   `8bo.   88ooo88 88    88 88oobY'    88    8P      88    88    88    `8bo.   
88 V8o88 88~~~~~ Y8   I8I   88 88  88  88     `Y8b. 88~~~88 88    88 88`8b      88    8b      88    88    88      `Y8b. 
88  V888 88.     `8b d8'8b d8' 88  88  88   db   8D 88   88 `8b  d8' 88 `88.    88    Y8b  d8 88b  d88    88    db   8D 
VP   V8P Y88888P  `8b8' `8d8'  YP  YP  YP   `8888Y' YP   YP  `Y88P'  88   YD    YP     `Y88P' ~Y8888P'    YP    `8888Y' 

'''

altgr = "3-"
ctrl = "C-"
alt = "A-"
HOME = "/home/klownie"
COPY_PASTE = f"{HOME}/.scripts/super_copy_paste.sh"
ROFI = f"{HOME}/.config/rofi/scripts"


class KeyBindings:
    def __init__(self, layout: Layout, mod: str, term: str) -> None:



        self.__layout = layout
        self.__term = term
        self.__super = mod + "-"



        self.__key_bindings = (


            # Newm focus mouvement :

            (alt + "S-Tab", lambda: self.__cycle_views(-1)),
            *((ctrl + str(i), lambda i=i: self.__goto_view(i)) for i in range(1, 11)),
            (self.__super + "h", lambda: self.__layout.move(-0.5, 0)),
            (self.__super + "j", lambda: self.__layout.move(0, 0.5)),
            (self.__super + "k", lambda: self.__layout.move(0, -0.5)),
            (self.__super + "l", lambda: self.__layout.move(0.5, 0)),
            (self.__super + "u", lambda: self.__layout.move(-0.5, -0.5)),
            (self.__super + "m", lambda: self.__layout.move(0.5, 0.5)),
            (self.__super + "i", lambda: self.__layout.move(0.5, -0.5)),
            (self.__super + "n", lambda: self.__layout.move(-0.5, 0.5)),
            (self.__super + "t", lambda: self.__layout.move_in_stack(4)),


            # Newm mouvement of windows :

            (self.__super + ctrl + "h",lambda: self.__layout.move_focused_view(-0.5, 0)),
            (self.__super + ctrl + "j", lambda: self.__layout.move_focused_view(0, 0.5)),
            (self.__super + ctrl + "k",lambda: self.__layout.move_focused_view(0, -0.5)),
            (self.__super + ctrl + "l", lambda: self.__layout.move_focused_view(0.5, 0)),


            #Newm window resizing :

            (self.__super + alt + "h",lambda: self.__layout.resize_focused_view(-0.5, 0)),
            (self.__super + alt + "j",lambda: self.__layout.resize_focused_view(0, 0.5)),
            (self.__super + alt + "k",lambda: self.__layout.resize_focused_view(0, -0.5)),
            (self.__super + alt + "l",lambda: self.__layout.resize_focused_view(0.5, 0)),


            #Other Newm focus mouvemnt :

            # (altgr + "w", self.layout.change_focused_view_workspace),
            (self.__super + "space", self.__layout.toggle_focused_view_floating),
            # ("Henkan_Mode", self.layout.move_workspace),
            (alt + "Tab", self.__cycle_views),
            (self.__super + "comma", lambda: self.__layout.basic_scale(0.5)),
            (self.__super + "period", lambda: self.__layout.basic_scale(-0.5)),
            (self.__super + "f", self.__layout.toggle_fullscreen),
            (self.__super + "p", lambda: self.__layout.ensure_locked(dim=True)),
            (self.__super + "P", self.__layout.terminate),
            (self.__super + "c", self.__layout.close_focused_view),
            (self.__super + "r", self.__layout.update_config),
            (self.__super,lambda: self.__layout.toggle_overview(only_active_workspace=True)),
            (altgr + "z", self.__layout.swallow_focused_view),


            #Playerctl shortcut :

            ("XF86AudioPrev", lambda: os.system("playerctl previous &")),
            ("XF86AudioNext", lambda: os.system("playerctl next &")),
            ("XF86AudioPlay", lambda: os.system("playerctl play-pause &")),


            #Terminal :

            (self.__super + "Return", lambda: os.system(self.__term + " &")),


            #Powermenu :

            (altgr + "e", lambda: os.system(f"{ROFI}/powermenu &")),


            #Clipboard :

            ("XF86Paste", self.__super_clipboard),
            ("XF86Copy", lambda: self.__super_clipboard("c")),
            ("XF86Open", lambda: os.system(f"{ROFI}/clipboard &")),


            #Bookmark :

            ("XF86Favorites", lambda: os.system(f"{ROFI}/bookmarks &")),


            #Password manager :

            # ("XF86Open", lambda: os.system(f"{self.ROFI}/passman &")),


            #Brightness :

            ("XF86MonBrightnessUp", lambda: os.system("brightnessctl set +2% &")),
            ("XF86MonBrightnessDown",lambda: os.system("brightnessctl set 2%- &")),
            # ("XF86KbdBrightnessUp",lambda: kbdlight_manager.set(kbdlight_manager.get() + 0.1)),
            # ("XF86KbdBrightnessDown", lambda: kbdlight_manager.set(kbdlight_manager.get() - 0.1)),


            #Mic :

            ("XF86AudioMicMute", lambda: os.system("volumectl -m toggle-mute &")),


            #Volume shortcut :

            ("XF86AudioRaiseVolume", lambda: os.system("volumectl -u up &")),
            ("XF86AudioLowerVolume", lambda: os.system("volumectl -u down &")),
            ("XF86AudioMute", lambda: os.system("volumectl toggle-mute &")),


            #Newm config edit shortcut :

            ("XF86Tools",lambda: os.system( self.__term + " nvim ~/.config/newm/config.py &")),
            ("XF86Tools",lambda: os.system( self.__term + " nvim ~/.config/newm/key_bindings.py &")),


            #App laucher :

            (self.__super + "d", lambda: os.system("tofi-drun --drun-launch=true &")),
            # (self.__super + "d", lambda: os.system(self.__term + " --title kitty_floats -e" + " fzf-run &")),
            # (self.__super + "d", lambda: os.system(self.__term + " --title kitty_floats -e" + " sway-launcher-desktop &")),
            (self.__super + "D", lambda: os.system(self.__term + " --title kitty_floats -e" + " dm-hub -f &")),
            # ("XF86LaunchA", lambda: os.system(f"{self.ROFI}/apps &")),


            #Screenshot shortcut :

            (self.__super + "s", lambda: os.system("shotman --capture output &")),
            (self.__super + "S",lambda: os.system("shotman --capture region &")),


            #Wifi manager :

            ("XF86Go", lambda: os.system(f"{ROFI}/wifi &")),


            #Email manager :

            ("XF86Mail",lambda: os.system("electron-mail --enable-features=UseOzonePlatform --ozone-platform=wayland &")),


            #Bluetooth manager :

            ("XF86Bluetooth", lambda: os.system("blueman-manager &")),


            #Volume manager :
            ("XF86AudioPreset", lambda: os.system("pavucontrol &")),

            #Other apps to lauch :

            (self.__super + "W", lambda: os.system("MOZ_ENABLE_WAYLAND=1 firefox &")),
            (self.__super + "F", lambda: os.system("nemo &")),
            (self.__super + "T", lambda: os.system(self.__term + " ranger &")),
        )



# Other fonctions that are used by 'Class KeyBindings'

    def __super_clipboard(self, key: str = "v"):
        view = self.__layout.find_focused_view()
        mode = " term" if view is not None and view.app_id == self.__term else ""
        os.system(f"{COPY_PASTE} {key}{mode} &")

    def __goto_view(self, index: int):
        if index == 0:
            return
        workspace = self.__layout.get_active_workspace()
        views = self.__layout.tiles(workspace)
        num_w = len(views)
        if index > num_w:
            return
        self.__layout.focus_view(views[index - 1])

    def __cycle_views(self, steps=1):
        workspace = self.__layout.get_active_workspace()
        views = tuple(self.__layout.tiles(workspace))
        current_view = self.__layout.find_focused_view()
        if not current_view or current_view not in views:
            return
        index = views.index(current_view) + steps
        self.__select_view(index, views)

    def __select_view(self, index: int, views: tuple[View]):
        num_w = len(views)
        index = (index + num_w) % num_w
        self.__layout.focus_view(views[index])

    def get(self):
        return self.__key_bindings
