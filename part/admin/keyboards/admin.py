from admin.keyboards.subclasses.rights import RightsKeyboard
from admin.keyboards.subclasses.subscriptions import SubscriptionKeyboard

from admin.models import Admin
from core.operations import KeyboardOperations


class AdminKeyboard(KeyboardOperations):
    def __init__(self):
        self.rights = RightsKeyboard()
        self.subscriptions = SubscriptionKeyboard()

    async def to_menu(self):
        buttons = {"<- Назад": "admin"}

        return await self.create_keyboard(buttons=buttons)

    async def menu(self, rights: str | Admin):
        buttons = {"Рассылка пользователям": "mailing"}

        if rights == "all":
            buttons["Подписки"] = "subscriptions"
            buttons["Админы"] = "rights"

        else:
            if rights.can_edit_admin:
                buttons["Админы"] = "rights"

            if rights.can_edit_subscription:
                buttons["Подписки"] = "subscriptions"

            if rights.can_block_user:
                buttons["Заблокировать пользователя"] = "block_user"

        return await self.create_keyboard(buttons=buttons)




