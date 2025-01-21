from core.operations import KeyboardOperations


class AdminKeyboard(KeyboardOperations):

    async def to_admin(self):
        buttons = {"Назад": "admin"}

        keyboard = await self.create_keyboard(buttons=buttons)
        return keyboard

    async def menu(self):
        buttons = {
            "Рассылка пользователям": "mailing",
        }

        keyboard = await self.create_keyboard(buttons=buttons)
        return keyboard

