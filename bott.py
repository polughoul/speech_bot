from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from voice import text_to_file
import requests

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    author_text = "Этого бота создал Андрей Стасюк.\nКонтакты: @Hero1nwat3r, e-mail: andreystasiuk1488@gmail.com"
    await update.message.reply_text(author_text)

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """Этот бот умеет\n 1. Преобразовывать текст в голос. Для этого напишите любое сообщение\n 
    2. Информация о авторе: введите /author\n 
    3. Отправлять картинку с котиком: введите /cat """
    await update.message.reply_text(help_text) 

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_name = text_to_file(update.message.text)
    await update.message.reply_voice(voice = open(file_name, "rb"))

async def cat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    # отправляем запрос к API сервиса CatAPI
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    # получаем ссылку на случайную картинку котика
    cat_url = response.json()[0]['url']
    # отправляем картинку пользователю в ответ на команду
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=cat_url)

app = ApplicationBuilder().token("").build()
#Для получения токена, воспользуйтесь телеграмм-ботом BotFather

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(CommandHandler("author", author))
app.add_handler(CommandHandler("cat", cat_handler))
app.run_polling()
