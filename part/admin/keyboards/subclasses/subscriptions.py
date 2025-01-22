from admin.models import Subscription
from core.operations import KeyboardOperations


class SubscriptionKeyboard(KeyboardOperations):

    async def to_menu(self):
        buttons = {"<- Назад": "subscriptions"}

        return await self.create_keyboard(buttons=buttons)

    async def menu(self):
        buttons = {
            "Добавить подписку": "add_subscription",
            "Список подписок": "subscriptions_list",
            "<- Назад": "admin"
        }

        return await self.create_keyboard(buttons=buttons)

    async def subscriptions_list(self, subscriptions: list[Subscription], payments: bool = False):
        buttons = dict()

        for subscription in subscriptions:
            if payments:
                buttons[f"{subscription.title} / {subscription.price}₽"] = f"payment_{subscription.id}"
            else:
                buttons[f"{subscription.title}"] = f"subscription_{subscription.id}"

        buttons["<- Назад"] = "subscriptions"
        return await self.create_keyboard(buttons=buttons)


