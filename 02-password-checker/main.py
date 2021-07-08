from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainContainer(BoxLayout):
    status_text = StringProperty("Enter a password")


class PasswordCheckerApp(App):
    pass


PasswordCheckerApp().run()
