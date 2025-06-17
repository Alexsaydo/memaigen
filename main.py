# main.py

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from generate_text import generate_meme_caption
from generate_image import generate_image

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("👋 Я ГенМем! Напиши мне идею мема — и я сделаю всё сам, с шуткой и картинкой!")

@dp.message_handler()
async def handle_text(message: types.Message):
    user_prompt = message.text
    await message.reply("Генерирую мем, жди 10–15 секунд...")

    try:
        caption = generate_meme_caption(user_prompt)
        image_url = generate_image(caption)
        await bot.send_photo(message.chat.id, photo=image_url, caption=caption)
    except Exception as e:
        await message.reply(f"Ошибка при генерации мема: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
