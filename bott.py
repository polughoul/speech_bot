
import getopt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, Updater, CallbackContext
from voice import text_to_file

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    author_text = "Этого бота создал Андрей Стасюк.\nКонтакты: @Hero1nwat3r, e-mail: andreystasiuk1488@gmail.com"
    await update.message.reply_text(author_text)

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = "Этот бот умеет\n 1. Преобразовывать текст в голос. Для этого напишите любое сообщение\n 2. Информация о авторе: введите /author\n 3. Отправлять картинку с котиком: введите /cat "
    await update.message.reply_text(help_text) 

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_name = text_to_file(update.message.text)
    #await update.message.reply_text(update.message.text.upper())
    await update.message.reply_voice(voice = open(file_name, "rb"))

async def cat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo(photo = open("C:\dev\speech_bot\data\kotik.jpg", 'rb'))




app = ApplicationBuilder().token("5826037486:AAGj9QrWywR_dFQvAeJVHPwAUIkPzu0PJ9c").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(CommandHandler("author", author))
app.add_handler(CommandHandler("cat", cat))
app.run_polling()

