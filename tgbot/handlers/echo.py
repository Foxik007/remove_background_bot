from aiogram import types, Dispatcher
from rembg import remove
from PIL import Image
from pathlib import Path



async def bot_echo(message: types.Message):
    text = [
        "Не понимаю что вы хотите",
        message.text
    ]

    await message.answer('\n'.join(text))

#======Основная логика проекта======
async def handle_docs_photo(message):

    await message.photo[-1].download(f'input_images/text.jpg')
    await message.reply('Пару секунд...')
    list_ex = ['*.png', '*.jpg']
    all_files = []

    for ext in list_ex:
        all_files.extend(Path('input_images').glob(ext))

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem
        output_path = f'output_images/{file_name}_output.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)
        print(f'Обработано: {index + 1}/{len(all_files)}')

        with open(output_path, 'rb') as photo:

            await message.reply_animation(photo, caption='Надеюсь тебе понравилось😇')


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(handle_docs_photo,content_types='photo')