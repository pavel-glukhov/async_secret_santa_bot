from aiogram import types
from aiogram.dispatcher.filters import Text

from app.bot import dispatcher as dp
from app.bot.handlers import text_messages
from app.store.database import room_db
from app.bot.keyborads.common import generate_inline_keyboard
from app.bot.handlers.operations import get_room_number


@dp.callback_query_handler(Text(startswith='room_config'))
async def configuration_room(callback: types.CallbackQuery):
    room_number = get_room_number(callback)
    keyboard_inline = generate_inline_keyboard(
        {
            "Изменить имя комнаты ⚒": f"room_change-name_{room_number}",
            "Изменить владельца 👤": f"room_change-owner_{room_number}",
            "Удалить комнату ❌": f"room_delete_{room_number}",
            "Вернуться назад ◀️": f"room_menu_{room_number}",
        }
    )
    room = await room_db().get(room_number)
    room_name = room.name
    
    await callback.message.edit_text(text_messages.CONFIG_ROOM_MENU.format(
        room_name, room_number,
    ),
        reply_markup=keyboard_inline, )
