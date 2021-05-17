import telebot
import pyowm

owm = pyowm.OWM('07e77770d88446d9d74b0e09296e74c5')
mgr = owm.weather_manager()

bot = telebot.TeleBot("1866009463:AAEFlBTMIZhvKpBzNCk5B92GvLWRsmgREwg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    observation = mgr.weather_at_place(message.text)
    w = observation.weather 
    temp = w.temperature('celsius')["temp"]

    answer = "Weather in " + message.text + " now " + w.detailed_status + ". Temperature: " + str(temp) + "\n"
    
    if temp < 10:
        answer += "It is cold now. Dress warmly!"
    elif temp < 20:
        answer += "It's warm enough now."
    else:
        answer += "The temperature is normal. Dress as you like."

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)