# from aiogram.types.message import ParseMode
# from app import dispatcher as dp
# from aiogram import types
#
# from app.database.config import async_session
# from app.database.operations import UserDB
# from app.misc.formatters import user_information_formatter
#
#
# @dp.message_handler(lambda message: message.text == "Мой профиль 👤")
# async def my_profile(message: types.Message):
#     edit_user_profile = types.InlineKeyboardButton(
#         text="Изменить профиль 👋",
#         callback_data="profile_edit"
#     )
#     keyboard_inline = types.InlineKeyboardMarkup().add(edit_user_profile)
#
#     async with async_session() as db_session:
#         async with db_session.begin():
#             user = await UserDB(
#                 db_session).get_user_or_none(user_id=message.chat.id)
#             user_information = await user_information_formatter(user)
#
#     await message.answer("Предоставленными вами данные необходимы для отправки"
#                          " подарка вашим Тайным Сантой.\n\n"
#                          "*Ваш профиль*:\n\n"
#                          f"{user_information}"
#                          "\n", parse_mode=ParseMode.MARKDOWN)
#     await message.answer("Если вы желаете изменить личные данные,"
#                          " или удалить их, нажмите на кнопку "
#                          "'Изменить профиль'",
#                          reply_markup=keyboard_inline)
#
#
# async def edit_profile(message: types.Message):
#     keyboard_inline = types.InlineKeyboardMarkup()
#     keyboard_list = [
#         types.InlineKeyboardButton(
#             text="Изменить имя",
#             callback_data="profile_edit_name"
#         ),
#         types.InlineKeyboardButton(
#             text="Изменить адрес",
#             callback_data="profile_edit_address"
#         ),
#         types.InlineKeyboardButton(
#             text="Изменить номер телефона",
#             callback_data="profile_edit_number"
#         ),
#         types.InlineKeyboardButton(
#             text="Удалить всю информацию ❌",
#             callback_data="profile_edit_delete_all"
#         ),
#     ]
#
#     for button in keyboard_list:
#         keyboard_inline.add(button)
#
#     await message.edit_text("Выберите, что вы хотите изменить:",
#                             reply_markup=keyboard_inline)
