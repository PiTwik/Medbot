import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv


TELEGRAM_TOKEN = '7038452791:AAEkylGmDtEN6Ek4E2Lhpd85gdDrhVUYBe4'

# Проверка, что токен загружен
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN не найден в файле .env")

# Определение клавиатуры с кнопками
keyboard = [
    ["Часы работы", "Контакты"],
    ["Запись на прием", "Обратная связь"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)


# Функция для команды /start
async def start(update: Update, context):
    welcome_message = (
        "Здравствуйте! Вы обратились в чат-бот поликлиники. "
        "Выберите действие из меню ниже:"
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


# Функция для обработки текстовых сообщений (включая нажатия кнопок)
async def handle_message(update: Update, context):
    user_message = update.message.text

    if user_message == "Часы работы":
        response = "Часы работы поликлиники: с 8:00 до 20:00 (Пн-Пт), с 9:00 до 15:00 (Сб)."  # Замените на реальные данные
        await update.message.reply_text(response, reply_markup=reply_markup)
    elif user_message == "Контакты":
        response = "Телефон единого центра обработки звонков: 8 (3022) 73-70-73 (многоканальный)"
        await update.message.reply_text(response, reply_markup=reply_markup)
    elif user_message == "Запись на прием":
        response = (
            "Для записи на прием укажите, пожалуйста, ваше ФИО, желаемую дату и специалиста. "
            "Я передам ваш запрос в колл-центр."
        )
        await update.message.reply_text(response, reply_markup=reply_markup)
    elif user_message == "Обратная связь":
        response = (
            "Благодарим за обращение! Оставьте ваш отзыв или сообщение — "
            "мы обязательно рассмотрим его."
        )
        await update.message.reply_text(response, reply_markup=reply_markup)
    else:
        response = "Пожалуйста, выберите действие из меню."
        await update.message.reply_text(response, reply_markup=reply_markup)


# Запуск бота
if __name__ == '__main__':
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    application.run_polling()git push -u origin main