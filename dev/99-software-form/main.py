from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dropdownitem import MDDropDownItem



class MainContainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(self.type_dropdown)
        menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)
        ]
        self.dropdown_item = None
        self.menu = MDDropdownMenu(
            caller=self.dropdown_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind()

    def handle_button_click(self):
        print(self.type_dropdown)
        print(dir(self.menu))
        self.menu.open()
    
    def set_item(self, text_item):
        print(f"set_item, text_item = {text_item}")
        self.ids.set_item(text_item)
        self.menu.dismiss()


class SoftwareForm(MDApp):
    pass


SoftwareForm().run()