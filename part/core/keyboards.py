from admin.keyboards.admin import AdminKeyboard
from menu.keyboards.menu import MenuKeyboard


class Keyboards:
    def __init__(self):
        self.admin = AdminKeyboard()
        self.menu = MenuKeyboard()

