from core.operations import KeyboardOperations


class MenuKeyboard(KeyboardOperations):
    async def menu(self):
        buttons = {
            "Задать вопрос": "ask_question",
            "FAQ": "FAQ"
        }

        keyboard = await self.create_keyboard(buttons=buttons)
        return keyboard
