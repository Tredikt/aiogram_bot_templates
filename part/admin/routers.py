from admin.handlers.command_handler import admin_command_router

from admin.handlers.mailing.callback_handler import mailing_callback_router
from admin.handlers.mailing.state_handler import mailing_state_router

from admin.handlers.rights.state_handler import rights_state_router
from admin.handlers.rights.callback_handler import rights_callback_router

from admin.handlers.subscriptions.state_handler import subscription_state_router
from admin.handlers.subscriptions.callback_handler import subscriptions_callback_router

admin_routers = [
    admin_command_router,

    mailing_state_router,
    mailing_callback_router,

    rights_state_router,
    rights_callback_router,

    subscriptions_callback_router,
    subscription_state_router,
]
