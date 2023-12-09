import logging
import wikipedia


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6951025966:AAHgvhik9XYiU3IUBc0fwG9SPz1_YaO8Fng'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalawma Alykum Siz bul botta sorawlarinizga juwap ala alasiz sorawlarinizga Qaraqalpaqsha juwap alasiz")



@dp.message_handler()
async def wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await  message.answer(respond)
    except:
        await  message.answer(" Bizlerde bunday magliwmat joq ")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)