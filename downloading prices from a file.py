from aiogram import Bot, Dispatcher, F
# класс бота, диспетчер обрабатывающий сообщения, класс с типом приходящего контента
from aiogram.types import Message, ContentType
# сообщение, класс с подготовленными возможными типами
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# создание клавы, создание кнопок клавы, удаление кнопок клавы
from aiogram.filters import Command, CommandStart, Text
# тип для фильтра - пришедшее сообщение команда(/....), команда старт, текст
import aiohttp
import pandas

service_file = open("service information.txt")
bot = Bot(token=service_file.readline().split()[1])
dp: Dispatcher = Dispatcher()
file_companies = open("info about companies.txt")
# <name>: <столбцы для скачивания через точку с запятой без пробелов>

async def process_start_command(message: Message):
    await message.answer('Бот готов к обработке excel файлов')

async def process_help_command(message: Message):
    await message.answer('Отправляйте excel файл выберите компанию, от которой данный файл. '
                         'Если компании нет в списке добавьте новую и выберите столбцы, которые '
                         'надо добавлять')

async def give_sql_command(message: Message):
    pass

async def send_doument(message: Message):
    await message.answer("Прислан документ на обработку")
    await download_excel(message.document.file_id)


async def download_excel(excel_file_id):
    file_info = await bot.get_file(excel_file_id)
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            content = await response.read()
            data_frame = pandas.read_excel(content, engine="openpyxl")
            print(data_frame.head())

# в диспетчере указывается, на какие сообщения, как реагировать
dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(give_sql_command, Command(commands=['give_sql']))
dp.message.register(send_doument, F.content_type == ContentType.DOCUMENT)

if __name__ == "__main__":
    dp.run_polling(bot)