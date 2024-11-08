from command_handlers import commands_routers
from callback_handlers import callback_routers
from states_handlers import states_routers

routers = [
    *commands_routers,
    *callback_routers,
    *states_routers
]