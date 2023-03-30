from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message :types.Message):
    try:        
        await bot.send_message(message.from_user.id , ' Рады видеть вас в нашем заведении, приятного аппетита', reply_markup= kb_client )
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС напишите ему: \n https://t.me/PIROGI_Zapolyarnyy_Bot')

# @dp.message_handler(commands=['Режим_работы'])
async def open_caffe(message :types.Message):
    await bot.send_message(message.from_user.id , ' Ежедневно с 11:00 до 23:00 часов ')

# @dp.message_handler(commands=['Расположение'])
async def maps_caffe(message :types.Message):
    await bot.send_message(message.from_user.id , ' Юбилейная ул., 2, Заполярный на против стамотологии')

def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'] )
    dp.register_message_handler(open_caffe, commands=['Режим_работы'])
    dp.register_message_handler(maps_caffe, commands=['Расположение'])


    