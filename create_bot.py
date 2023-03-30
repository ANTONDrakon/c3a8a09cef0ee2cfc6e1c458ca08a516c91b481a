from aiogram import Bot , Dispatcher ,  types
TOKEN = '5972357173:AAHQVF8W89PcfqBcP_NvDphHWdyM96vtIAw'
bot = Bot(token = TOKEN)
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

dp = Dispatcher(bot = bot, storage=storage)