from ..operations import KeyboardOperations


class AdminKeyboard(KeyboardOperations):

    async def back_to_admin(self):
        buttons = {"Назад": "admin"}

        keyboard = await self.create_base_keyboard(buttons=buttons)
        return keyboard

    async def admin_menu(self):
        buttons = {
            "Рассылка пользователям": "mailing_to_users",
        }

        keyboard = await self.create_base_keyboard(buttons=buttons)
        return keyboard

