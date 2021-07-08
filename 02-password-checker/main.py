from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainContainer(BoxLayout):
    status_text = StringProperty("Enter a password")

    def handle_check_button_press(self):
        print("Check button was pressed!")


class PasswordCheckerApp(App):
    pass


PasswordCheckerApp().run()
