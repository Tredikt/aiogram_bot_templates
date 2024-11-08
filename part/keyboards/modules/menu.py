from ..operations import KeyboardOperations


class MenuKeyboard(KeyboardOperations):
    async def menu(self):
        buttons = {
            "Задать вопрос": "ask_question",
            "FAQ": "FAQ"
        }

        keyboard = await self.create_base_keyboard(buttons=buttons)
        return keyboard
