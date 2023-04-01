from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


file = open("service information.txt")
bot = Bot(token=file.readline().split()[1])
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

@dp.message()
async def send_echo(message: Message):
    await message.answer(message.text)


if __name__ == "__main__":
    dp.run_polling(bot)