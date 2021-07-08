from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainContainer(BoxLayout):
    status_text = StringProperty("Enter a password")

    def handle_check_button_press(self, password):
        print("Check button was pressed!")
        print(f"Password: {password}")

        score = self.calc_password_score(password)
        print(f"Score: {score}")

        if score >= 40:
            self.status_text = "Strong"
        elif score >= 20:
            self.status_text = "Moderate"
        elif score >= 0:
            self.status_text = "Weak"
        else:
            self.status_text = "Invalid"

    def handle_info_button_press(self):
        print("Info button was pressed!")
    
    def calc_password_score(self, password):
        """
        The password will get 10pts for each criteria present:
        - length > 8
        - contains lower-case letters
        - contains upper-case letters
        - contains numbers
        - contains symbols

        A password cannot contain a space or be less than 6 characters. 
        If so, return -1 (invalid).
        """
        return 0


class PasswordCheckerApp(App):
    pass


PasswordCheckerApp().run()
