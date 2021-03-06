from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty


INFORMATION = """A secure password should...
- Criteria 1
- Criteria 2
- Criteria 3
- Etc..
"""

class MainContainer(RelativeLayout):
    status_text = StringProperty("Enter a password")
    information_text = StringProperty(INFORMATION)

    def handle_check_button_press(self, password):
        score = self.calc_password_score(password)
        if score >= 40:
            self.status_text = "Strong"
        elif score >= 20:
            self.status_text = "Moderate"
        elif score >= 0:
            self.status_text = "Weak"
        else:
            self.status_text = "Invalid"

    def handle_info_button_press(self):
        self.information_overlay.show()
    
    def calc_password_score(self, password):
        """
        The password will get 10pts for each criteria present:
        - length >= 8
        - contains lower-case letters
        - contains upper-case letters
        - contains numbers
        - contains symbols

        A password cannot contain a space or be less than 6 characters. 
        If so, return -1 (invalid).
        """
        score = 0

        if len(password) < 6 or " " in password:
            return -1

        if len(password) >= 8:
            score += 10

        has_lower = False
        has_upper = False
        has_number = False
        has_symbol = False

        for c in password:
            # ASCII values
            # lower: 97-122
            # upper: 65-90
            # numbers: 48-57
            # symbols: 33-64, 91-96, 123-126

            ascii_value = ord(c)

            if ascii_value >= 97 and ascii_value <= 122:
                has_lower = True
            elif ascii_value >= 65 and ascii_value <= 90:
                has_upper = True
            elif ascii_value >= 48 and ascii_value <= 57:
                has_number = True
            elif (ascii_value >= 33 and ascii_value <= 64 or
                  ascii_value >= 91 and ascii_value <= 96 or
                  ascii_value >= 123 and ascii_value <= 126):
                has_symbol = True
        
        score += (int(has_lower) + int(has_upper) + int(has_number) + int(has_symbol)) * 10

        return score


class InformationOverlay(BoxLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super().on_touch_down(touch)
    
    def handle_info_back_button_press(self):
        self.opacity = 0
    
    def show(self):
        self.opacity = 1


class PasswordCheckerApp(App):
    pass


PasswordCheckerApp().run()
