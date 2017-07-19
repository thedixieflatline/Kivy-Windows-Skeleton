# Python Console Control

s = 'SLOTSIM PYTHON SCRIPT START'
n = ''
print(s)
print(n)

# Python library import

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Class declaration
class Interface(BoxLayout):
    pass
# Application loop

class SlotsimApp(App):
    def build(self):
        root_widget = Interface()
        return root_widget
        # game = ButtonTest()
        # return game

# Application run
if __name__ == '__main__':
    SlotsimApp().run()