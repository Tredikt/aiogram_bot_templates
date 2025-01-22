from admin.models import Admin
from core.operations import KeyboardOperations


class RightsKeyboard(KeyboardOperations):

    async def to_rights(self):
        buttons = {"<- Назад": "rights"}

        return await self.create_keyboard(buttons=buttons)

    async def admins(self):
        buttons = {
            "Добавить админа": "add_admin",
            "Список админов": "admins_list",
            "<- Назад": "admin"
        }

        return await self.create_keyboard(buttons=buttons)

    async def admins_list(self, admins: list[Admin]):
        buttons = dict()
        for admin in admins:
            buttons[f"{admin.user.full_name}"] = f"admin_{admin.user_id}"

        buttons["<- Назад"] = "rights"
        return await self.create_keyboard(buttons=buttons)

    async def admin_rights(self, admin: Admin):
        can_edit_admin = "✅" if admin.can_edit_admin else "❌"
        can_edit_subscription = "✅" if admin.can_edit_subscription else "❌"

        buttons = {
            f"Может редактировать админов {can_edit_admin}": f"can_edit_admin_{admin.user_id}",
            f"Может редактировать подписки {can_edit_subscription}": f"can_edit_subscription_{admin.user_id}",
            f"Удалить админа": f"delete_admin_{admin.user_id}",
            "<- Назад": "admin"
        }

        return await self.create_keyboard(buttons=buttons)

