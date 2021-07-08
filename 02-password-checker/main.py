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
            print(c, ascii_value)

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
        
        print(f"{has_lower = }")
        print(f"{has_upper = }")
        print(f"{has_number = }")
        print(f"{has_symbol = }")

        
        return score


class PasswordCheckerApp(App):
    pass


PasswordCheckerApp().run()
