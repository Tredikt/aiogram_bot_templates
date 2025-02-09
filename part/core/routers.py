from core.handlers.my_id_handler import my_id_router
from core.utils import configure_router

from admin.routers import admin_routers
from menu.routers import menu_routers

routers = [
    configure_router,
    my_id_router,
    *admin_routers,
    *menu_routers
]
