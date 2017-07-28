# Python Console Control

s = 'SLOTSIM PYTHON SCRIPT START'
n = ''
print(s)
print(n)

# SET KIVY HOME TO BE THE GAME FOLDER
import os
print('SET KIVY HOME')
os.environ['KIVY_HOME'] = 'Games\Default\\'
print(os.environ['KIVY_HOME'])

# SET KIVY CONFIG OPTIONS Kivy App options set automatically to Config
from kivy.config import Config
from kivy.config import ConfigParser

# window_state: string , one of ‘visible’, ‘’, ‘maximized’
Config.set('graphics', 'window_state', 'visible')
# TURN ON OR OFF WRITING KIVY LOG FILES AND TUNE VERBOCITY
# log_enable = 1
Config.set('kivy', 'log_enable', 0)

# Different logging levels are available : trace, debug, info, warning, error and critical.
Config.set('kivy', 'log_level', 'info')
# set screen size
Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
# write the config options
Config.write()

# Create the Sim project objects and file configuration locations
SymbolsConfig = ConfigParser(name='Symbols')
SymbolsConfig.read(os.environ['KIVY_HOME'] + 'Default-Symbols.ini')

ReelsConfig = ConfigParser(name='Reels')
ReelsConfig.read(os.environ['KIVY_HOME'] + 'Default-Reels.ini')

# SET GAME CONFIG OPTIONS
import json
print(json.dumps({'GameName': 'Slot Sim', 'Version': "0.1"}, sort_keys=True, indent=4))

# import the external python file settingsjson.py
from symbolsjson import symbols_json
from reelsjson import reels_json
# Library Import

# PYTHON
from random import random

# Kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.event import EventDispatcher
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.settings import SettingsWithTabbedPanel


# Load the KV file for the game
Interface = Builder.load_file("slotsim.kv")

# Class declaration ?????????????????????????????????????????????????????????????????

# Declare screen classes


class GameScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class SimulatorScreen(Screen):
    pass


# Screen Manager setup &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Create the screen manager
ScreenSystem = ScreenManager()

# Add screens to screen manager
ScreenSystem.add_widget(GameScreen(name='GameScreen'))
ScreenSystem.add_widget(SettingsScreen(name='SettingsScreen'))
ScreenSystem.add_widget(SimulatorScreen(name='SimulatorScreen'))


# Application loop @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class SlotsimApp(App):

    def build(self):
        self.title = 'Slot Simulator'
        self.icon = 'Games\Default\Images\custom-kivy-icon.png'
        self.settings_cls = SettingsWithTabbedPanel
        self.use_kivy_settings = True
        return ScreenSystem

    def on_start(self):
        Logger.info('App: I\'m alive!')

    def on_stop(self):
        Logger.critical('App: Aaaargh I\'m dying!')

    def build_config(self, config):
        SymbolsConfig.setdefaults('screen', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option1',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})
        ReelsConfig.setdefaults('screen', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option1',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})

    def build_settings(self, settings):
        # import the external python file settingsjson.py
        settings.add_json_panel('Symbols', SymbolsConfig, data=symbols_json)
        settings.add_json_panel('Reels', ReelsConfig, data=reels_json)

    def on_config_change(self, config, section, key, value):
        print(ReelsConfig, section, key, value)
        print(SymbolsConfig, section, key, value)

if __name__ == '__main__':
    SlotsimApp().run()

    # Examples before implimentation if you know what I mean!
    # <DrawingWidget>:
    #     canvas:
    #         Color:
    #             rgba: 1, 1, 1, 1
    #         Rectangle:
    #             pos: self.pos
    #             size: self.size
    #             #size: (50, 50)
    #
    # <ColourSlider@Slider>:
    #     min: 0
    #     max: 1
    #     value: 0.5
    #     size_hint_y: None
    #     height: 80

    # <Interface>:
    #     orientation: 'vertical'
    #     Button:
    #         Image:
    #             source: 'Games/Default/Images/Button_Base_Oval_Normal.png'
    #             #y: self.parent.y + self.parent.height - 250
    #             #x: self.parent.x
    #             center_x: self.parent.center_x
    #             center_y: self.parent.center_y
    #             size: 250, 250
    #             allow_stretch: True
    #         Label:
    #             text: "Spin"
    #     Label:
    #         text: "Spin"

    #	background_color: 80,50,40,0.5
    #	size: 100,75
    #	pos: 0,0
    #	text: str(self.state)
    #	color: 20,100,0,1
    #	font_size: 40

    # BoxLayout:
    #    orientation: 'horizontal'
    #    size_hint_y: None
    #    height: 140
    #    Label:
    #        text: 'output colour:'

    # class DrawingWidget(Widget):
    #
    #     def on_touch_down(self, touch):
    #         super(DrawingWidget, self).on_touch_down(touch)
    #
    #         if not self.collide_point(*touch.pos):
    #             return
    #
    #         with self.canvas:
    #             Color(random(), random(), random())
    #             self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)
    #
    #     def on_touch_move(self, touch):
    #         if not self.collide_point(*touch.pos):
    #             return
    #
    #         self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]

    # class Interface(BoxLayout):
    #     pass
