from typing import Type
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu


class CustomDropDown(RelativeLayout):
    pass


class MainContainer(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = CustomDropDown()
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]

        self.menu = MDDropdownMenu(
            caller=self.dropdown.ids.field,
            items=menu_items,
            width_mult=4,
            # pos_hint={"x": self.dropdown.center_x, "y": self.dropdown.center_y}
        )
    
    def menu_callback(self, text):
        self.dropdown.field.set_item(text)
        self.dropdown.field.text = "Blah"
        self.menu.dismiss()
    

class DropApp(MDApp):
    pass


DropApp().run()