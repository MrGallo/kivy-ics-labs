from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class NameAndAgeApp(MDApp):
    dialog = None
    def show_alert_dialog(self, name: str, age: str) -> None:
        # print("Button pressed")
        # print(f"{name = }")
        # print(f"{age = }")

        
        self.dialog = MDDialog(
            title="About you",
            text=f"Name: {name}\nAge: {age}",
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.hide_alert_dialog
                )
            ],
        )
        self.dialog.open()
    
    def hide_alert_dialog(self, widget):
        self.dialog.dismiss(force=True)


NameAndAgeApp().run()
