#TELEGRAM BOT - МОЖЕТ ВЫВЕСТИ ПОГОДУ В ЛЮБОМ ГОРОДЕ. ПРОСТО НАПИШИТЕ НАЗВАНИЕ ГОРОДА ЕМУ В ЛИЧНОЕ СООБЩЕНЕ (Для начала работы введите команду /start)

from pyowm import OWM
from translate import Translator
import telebot #МОДУЛЬ ДЛЯ СОЗДАНИЯ БОТА В TELEGRAM
import config  #СОБСТВ. МОДУЛЬ С НЕЗНАЧИТЕЛЬНЫМИ ПЕРЕМЕННЫМИ

translator = Translator(to_lang="Russian") # изначально данные о погоде выводятся на английском, поэтому пришлось переводить с помощью данной строки

owm = OWM('7f0fb6e211ca80b8042a2197c3030206') #работа с погодой
mgr = owm.weather_manager()
bot = telebot.TeleBot(config.TOKEN) #ПРИСВАИВАНИЕ ТЕГА БОТА

@bot.message_handler(commands=['start']) #комманда /start
def welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вас приветствует weather_telegrambot. Введите надвание города в котором хотите узнать погоду.')

@bot.message_handler(content_types=["text"]) #ХЕНДЛЕР КОМАНДЫ
def send_welcome(message):
    place = message.text
    observation = mgr.weather_at_place(place)
    w = observation.weather
    translation_status = translator.translate(w.detailed_status)#Перевод статуса города на Рус.Яз.
    temperature = str(w.temperature('celsius'))#Присваиваем строку модуля с температурами
    schet = int(temperature.find(","))#Находим первую запятую в этой строке 
    restemp = str(temperature[8:schet])#результат температуры
    answer = ' Температура в городе ' + str(place) + ' сейчас: ' + restemp + ' (по цельсию)'+'\n'
    answer += ' Статус города: '+str(translation_status)+'\n\n'#Вывод  статуса города
    bot.send_message(message.chat.id, answer)#вывод результата в мессенджер бота


bot.infinity_polling() #БЕСКОНЕЧНЫЙ ЦИКЛ