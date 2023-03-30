from aiogram import executor 
from create_bot import dp


async def on_startup(_):
    print('бот вышел в онлайн')


from handlers import client, admin, other
client.register_hendlers_client(dp)
admin.register_hendlers_admin(dp)
other.register_hendlers_other(dp)








executor.start_polling(dp, skip_updates=True, on_startup=on_startup)





