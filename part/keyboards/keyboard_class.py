from .modules import (
    AdminKeyboard,
    MenuKeyboard
)


class Keyboards:
    def __init__(self):
        self.admin = AdminKeyboard()
        self.menu = MenuKeyboard()

