from aiogram import types


kb_menu = [
    [
        types.KeyboardButton(text='Начало и конец дня', resize_keyboard=True),
        types.KeyboardButton(text='Список кодов', resize_keyboard=True),
        types.KeyboardButton(text='Изменение кодов', resize_keyboard=True),
        types.KeyboardButton(text='Расписание предыдущих дней', resize_keyboard=True),
        #types.KeyboardButton(text='Прекращение работы', resize_keyboard=True),
        types.KeyboardButton(text='Начать работу с расписанием', resize_keyboard=True)
    ]
]

kb_menu_change_codes = [
    [
        types.KeyboardButton(text='Список кодов', resize_keyboard=True),
        types.KeyboardButton(text='Добавить код', resize_keyboard=True),
        types.KeyboardButton(text='Удалить код', resize_keyboard=True),
        types.KeyboardButton(text='Удалить все коды', resize_keyboard=True),
        types.KeyboardButton(text='Вернуться в меню', resize_keyboard=True)
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
        types.KeyboardButton(text='Изменить начало дня', resize_keyboard=True),
        types.KeyboardButton(text='Изменить конец дня', resize_keyboard=True)
    ]
]