from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from database.orm import SyncOrm
from keyboards.address_kb import address_kb
from keyboards.cancel_kb_adm import cancel_kb_adm
from states.create_address import AdminAddAddress
from keyboards.admin_kb import admin_menu_kb
from states.delete_address import AdminDeleteAddress
from utils.address_checker import is_valid_solana_address
from utils.log_config import bot_logger as logger
from database.models import Address, User

router = Router()


# /admin
@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    logger.info(f"{message.from_user.username} {message.from_user.id} press call /admin")

    if not SyncOrm.is_admin(message.from_user.id):
        return await message.answer("⚠️ У вас нет доступа.")

    await message.answer("Админ-панель:", reply_markup=admin_menu_kb())
    return None


# Callback "Добавить адрес"
@router.callback_query(F.data == "adm_address")
async def add_address_start(callback: CallbackQuery, state: FSMContext):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button Адреса")

    if not SyncOrm.is_admin(callback.from_user.id):
        return await callback.answer("⚠️ Нет доступа", show_alert=True)

    # await state.set_state(AdminAddAddress.waiting_for_address)
    await callback.message.answer("Операции с кошельками:", reply_markup=address_kb())
    return await callback.answer()



# добавляем
@router.callback_query(F.data == "adm_add_address")
async def add_address_callback(callback: CallbackQuery, state: FSMContext):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button adm_add_address")

    if not SyncOrm.is_admin(callback.from_user.id):
        return await callback.answer("⚠️ Нет доступа", show_alert=True)

    await state.set_state(AdminAddAddress.waiting_for_address)
    await callback.message.answer("Введите адрес кошелька USDT (SOL)", reply_markup=cancel_kb_adm())
    await callback.answer()

    return None


# Приём нового адреса
@router.message(AdminAddAddress.waiting_for_address)
async def add_address_finish(message: Message, state: FSMContext):
    addr = message.text.strip()

    # простая проверка
    if not is_valid_solana_address(addr):
        return await message.answer("⚠️ Некорректный Solana-адрес, попробуйте ещё раз.", reply_markup=cancel_kb_adm())

    if SyncOrm.get_address_by_address(addr):
        return await message.answer("⚠️ Кошелек с таким адресом уже существует", reply_markup=cancel_kb_adm())

    SyncOrm.add_address(addr)

    await state.clear()
    await message.answer(
        f"Адрес <code>{addr}</code> успешно добавлен! ✅",
        reply_markup=address_kb()
    )

    return None


# Выводим все адреса
@router.callback_query(F.data == "adm_show_address")
async def show_address_callback(callback: CallbackQuery, state: FSMContext):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button adm_show_address")


    if not SyncOrm.is_admin(callback.from_user.id):
        return await callback.answer("Нет доступа", show_alert=True)


    addresses = SyncOrm.get_addresses()

    text = ''
    for address in addresses:
        text += f'{address.id}. <code>{address.address}</code>\nБАЛАНС: {address.balance}$\n\n'

    await callback.message.answer(text, reply_markup=address_kb())
    await callback.answer()
    return None


# удаляем адрес
@router.callback_query(F.data == "adm_del_address")
async def start_del_address_callback(callback: CallbackQuery, state: FSMContext):
    logger.info(f"{callback.from_user.username} {callback.from_user.id} press button adm_del_address")

    if not SyncOrm.is_admin(callback.from_user.id):
        return await callback.answer("⚠️ Нет доступа", show_alert=True)

    await state.set_state(AdminDeleteAddress.waiting_for_address)
    await callback.message.answer("Введите адрес кошелька", reply_markup=cancel_kb_adm())
    await callback.answer()

    return None


@router.message(AdminDeleteAddress.waiting_for_address)
async def delete_address_callback(message: Message, state: FSMContext):
    addr = message.text.strip()

    if not SyncOrm.get_address_by_address(addr):
        return await message.answer("⚠️ Кошелек с таким адресом не существует", reply_markup=cancel_kb_adm())

    SyncOrm.delete_address(addr)

    await state.clear()
    await message.answer(
        f"Адрес <code>{addr}</code> успешно удалён!",
        reply_markup=address_kb()
    )
    return None


@router.callback_query(F.data == 'adm_back')
async def back_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Админ-панель:", reply_markup=admin_menu_kb())
    await callback.answer()



@router.callback_query(F.data == "admin_cancel")
async def admin_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Действие отменено.")
    await callback.message.answer("Админ-панель:", reply_markup=admin_menu_kb())
    await callback.answer()
