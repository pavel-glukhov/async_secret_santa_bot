import math
from typing import Any

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Pagination:
    def __init__(
            self, objects: Any,
            page_size: int,
            callback_next_prefix: str,
            callback_back_prefix: str,
            callback_prefix: str,
            keyboard_name_or_method: str | None = None,
            callback_name_or_method: str | None = None
    ):
        self.objects = objects
        self.page_size = page_size
        self.callback_next_prefix = callback_next_prefix
        self.callback_back_prefix = callback_back_prefix
        self.callback_prefix = callback_prefix
        self.keyboard_name_or_method = keyboard_name_or_method
        self.callback_name_or_method = callback_name_or_method
    
    def inline_pagination(self, page: int):
        data = self._data_splitter(page, self.objects)
        collection = data.get('collection')
        total_pages = data.get('total_pages')
        end_index = data.get('end_index')
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        
        for item in collection:
            if self.keyboard_name_or_method:
                keyboard_text = getattr(item, self.keyboard_name_or_method)
            else:
                keyboard_text = item
            
            if self.callback_name_or_method:
                callback_query = getattr(item, self.callback_name_or_method)
            else:
                callback_query = item
            
            button = InlineKeyboardButton(
                text=keyboard_text,
                callback_data=(
                    f'{self.callback_prefix}:{callback_query}'
                )
            )
            keyboard_markup.insert(button)
        
        count_button = InlineKeyboardButton(
            f'({page}/{total_pages})', callback_data='non_click_count_pages'
        )
        empty_button = InlineKeyboardButton(
            '  ', callback_data='non_click_button_disabled'
        )
        prev_button = InlineKeyboardButton(
            text='◀️', callback_data=f'{self.callback_back_prefix}:{page}'
        )
        next_button = InlineKeyboardButton(
            text='➡️', callback_data=f'{self.callback_next_prefix}:{page}'
        )
        if len(self.objects) > self.page_size:
            if page == 1 and page < end_index < len(self.objects):
                keyboard_markup.row(empty_button, count_button, next_button)
            
            if 1 < page < end_index < len(self.objects):
                keyboard_markup.row(prev_button, count_button, next_button)
            
            if page > 1 and page == total_pages:
                keyboard_markup.row(prev_button, count_button, empty_button)
        
        return keyboard_markup
    
    def _data_splitter(self, page: int, objects: list[Any]) -> dict:
        start_index = (page - 1) * self.page_size
        end_index = start_index + self.page_size
        total_pages = math.ceil(len(objects) / self.page_size)
        return {
            'collection': objects[start_index:end_index],
            'total_pages': total_pages,
            'start_index': start_index,
            'end_index': end_index
        }
