from aiogram import types, Dispatcher
from create_bot import dp
from aiogram import types
import string
import json


# @dp.message_handler()
async def echo_send(message :types.Message):
    if {i.lower().translate(str.maketrans('' ,'' , string.punctuation))for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))):
        await message.reply(" Маты запрещены !!!")
        await message.delete()
def register_hendlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
