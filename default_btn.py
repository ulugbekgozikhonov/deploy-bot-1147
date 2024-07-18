from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share Contact", request_contact=True)
        ]
    ],resize_keyboard=True
)



shop_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("My Orders"),
            KeyboardButton("Books Shop"),
        ],
        [
            KeyboardButton("My Books"),
            KeyboardButton("Profile"),
        ]
    ],resize_keyboard=True
)