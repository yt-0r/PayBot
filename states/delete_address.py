# states/admin_states.py
from aiogram.fsm.state import State, StatesGroup

class AdminDeleteAddress(StatesGroup):
    waiting_for_address = State()
