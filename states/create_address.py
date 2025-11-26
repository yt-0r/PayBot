# states/admin_states.py
from aiogram.fsm.state import State, StatesGroup

class AdminAddAddress(StatesGroup):
    waiting_for_address = State()
