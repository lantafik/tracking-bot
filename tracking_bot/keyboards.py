from aiogram import types

kb_ak = [
    [
        types.KeyboardButton(text='/register', resize_keyboard=True),
        types.KeyboardButton(text='/log_in', resize_keyboard=True),
    ]
]

kb_menu = [
    [
        types.KeyboardButton(text='/day_settings', resize_keyboard=True),
        types.KeyboardButton(text='/List_of_codes', resize_keyboard=True),
        types.KeyboardButton(text='/Changing_codes', resize_keyboard=True),
        types.KeyboardButton(text='/Schedule_history', resize_keyboard=True),
        #types.KeyboardButton(text='Прекращение работы', resize_keyboard=True),
        types.KeyboardButton(text='/Start_of_the_schedule', resize_keyboard=True)
    ]
]

kb_menu_change_codes = [
    [
        types.KeyboardButton(text='/Add_a_code', resize_keyboard=True),
        types.KeyboardButton(text='/Delete_the_code', resize_keyboard=True),
        types.KeyboardButton(text='/Delete_all_codes', resize_keyboard=True),
        types.KeyboardButton(text='/Go_back_to_the_menu', resize_keyboard=True)
    ]
]

kb_menu_reg_codes = [
    [
        types.KeyboardButton(text='/Add_a_code', resize_keyboard=True),
    ]
]

kb_menu_codes = [
    [
        types.KeyboardButton(text='Меню изменения кодов', resize_keyboard=True),
        types.KeyboardButton(text='Начать работу с расписанием', resize_keyboard=True),
        types.KeyboardButton(text='Основное меню', resize_keyboard=True)
    ]
]

kb_menu_start_and_end_day = [
    [
        types.KeyboardButton(text='Посмотреть время начала и конца дня', resize_keyboard=True),
        types.KeyboardButton(text='Изменить начало дня', resize_keyboard=True),
        types.KeyboardButton(text='Изменить конец дня', resize_keyboard=True)
    ]
]

kb_menu_start_and_end_day_2 = [
    [
        types.KeyboardButton(text='/Change_the_start_of_the_day', resize_keyboard=True),
        types.KeyboardButton(text='Изменить конец дня', resize_keyboard=True)
    ]
]