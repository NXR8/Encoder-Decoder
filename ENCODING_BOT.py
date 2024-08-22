import time
import telebot, base64
from telebot import types
import logging

encoded = {
  "0": ".$.0",
  "1": "/@]5",
  "2": ".#(7",
  "3": ".}!5",
  "4": "/}]2",
  "5": "/+?4",
  "6": "/&[4",
  "7": ".!!6",
  "8": "*/..",
  "9": "/(/.",
  "a": ".,/2",
  "A": ".,/@",
  "b": "/.8/",
  "B": "/.*/",
  "c": "//.1",
  "C": "//.!",
  "d": "//,4",
  "D": "//,$",
  "e": "./,3",
  "E": "./,#",
  "f": "./,5",
  "F": "./,%",
  "g": "./,9",
  "G": "./,(",
  "h": "./,7",
  "H": "./,&",
  "i": "./,1",
  "I": "./,!",
  "j": "./,6",
  "J": "./,^",
  "k": "./,2",
  "K": "./,@",
  "l": "./,8",
  "L": "./,*",
  "m": "./,4",
  "M": "./,$",
  "n": "./,0",
  "N": "./,,",
  "o": "//.0",
  "O": "//.,",
  "p": "//.2",
  "P": "//.@",
  "q": "//.9",
  "Q": "//.(",
  "r": "//.6",
  "R": "//.^",
  "s": "//.5",
  "S": "//.%",
  "t": "//.7",
  "T": "//.&",
  "u": "//.4",
  "U": "//.$",
  "v": "//.8",
  "V": "//.*",
  "w": "//.3",
  "W": "//.#",
  "x": "/./8",
  "X": "/./*",
  "y": "/./7",
  "Y": "/./&",
  "z": "/,/2",
  "Z": "/,/@",
}

decoded = {y: x for x, y in encoded.items()}

encode = lambda text: "".join(
  [encoded[x] for x in base64.b16encode(text.encode()).decode()])


def decode(text):
  data = []
  nm = 0
  for x in range(len(text) // 4):
    data.append(text[nm:nm + 4])
    nm += 4
  return base64.b16decode("".join([decoded[x] for x in data]).encode()).decode()


token = "<your_telegram_bot_tokek>"
bot = telebot.TeleBot(token)
ID = <your_ID>

markup = types.InlineKeyboardMarkup()

##############################################################################################################################
@bot.message_handler(commands=["ny"])
def ny(message):
  try:
    msg = message.text
    msg = msg.replace("/ny", "").strip()

    if message.reply_to_message:
        replied_message = message.reply_to_message.text
        msg = encode(replied_message)
    else:
        text_message = message.text.replace("/ny", "").strip()
        msg = encode(text_message)

    bot.reply_to(message, msg, reply_markup=markup)

  except:
    bot.reply_to(message, "The bot can't encode this message, please check if there is an error in it.", reply_markup=markup)
    try:
      bot.send_message(
        ID,
        "The error and user info: " + "\n\n" + "User name: @" +
        str(message.from_user.username) + "\n" + "Name: " +
        str(message.from_user.first_name) + " " + message.from_user.last_name +
        "\n" + "ID: " + str(message.chat.id) + "\n" + "Premium: " +
        str(message.from_user.is_premium) + "\n\n" + "Message: " +
        message.text,
      )
    except:
      bot.send_message(
        ID,
        "The error and user info: " + "\n\n" + "User name: @" +
        str(message.from_user.username) + "\n" + "Name: " +
        str(message.from_user.first_name) + "\n" + "ID: " +
        str(message.chat.id) + "\n" + "Premium: " +
        str(message.from_user.is_premium) + "\n\n" + "Message: " +
        message.text,
      )
  print("Name: " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + "\tID: " + str(message.chat.id) + "\t\tMessage: " + str(message.text))

##############################################################################################################################

@bot.message_handler(commands=["text"])
def toText(message):
  try:
    msg = message.text
    msg = msg.replace("/text", "").strip()
    # bot.reply_to(message, decode(msg), reply_markup=markup)
    if message.reply_to_message:
        replied_message = message.reply_to_message.text
        msg = decode(replied_message)
    else:
        text_message = message.text.replace("/text", "").strip()
        msg = decode(text_message)

    bot.reply_to(message, msg, reply_markup=markup)

  except:
    bot.reply_to(message, "The bot can't decode this message, please check if there is an error in it.", reply_markup=markup)
    try:
      bot.send_message(
        ID,
        "The error and user info: " + "\n\n" + "User name: @" +
        str(message.from_user.username) + "\n" + "Name: " +
        str(message.from_user.first_name) + " " + message.from_user.last_name +
        "\n" + "ID: " + str(message.chat.id) + "\n" + "Premium: " +
        str(message.from_user.is_premium) + "\n\n" + "Message: " +
        message.text,
      )
    except:
      bot.send_message(
        ID,
        "The error and user info: " + "\n\n" + "User name: @" +
        str(message.from_user.username) + "\n" + "Name: " +
        str(message.from_user.first_name) + "\n" + "ID: " +
        str(message.chat.id) + "\n" + "Premium: " +
        str(message.from_user.is_premium) + "\n\n" + "Message: " +
        message.text,
      )
  print("Name: " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + "\tID: " + str(message.chat.id) + "\t\tMessage: " + str(message.text))

##############################################################################################################################

@bot.message_handler(commands=["start"])
def start(message):
  ide = message.from_user.first_name
  bot.reply_to(
    message,
    "Hi " + ide + " This bot is made by @NXR81 and @O0O0I" + "\n\n" +
    "for encryption type " + "/ny [the text you want to encrypt]" + "\n" +
    "like: " + "/ny NXR8", reply_markup=markup
  )
  bot.send_message(message.chat.id, "/ny NXR8")
  bot.send_message(message.chat.id, "Will be the output")
  bot.send_message(message.chat.id, encode("NXR8"))
  try:
    bot.send_message(
      ID,
      "The error and user info: " + "\n\n" + "User name: @" +
      str(message.from_user.username) + "\n" + "Name: " +
      str(message.from_user.first_name) + " " + message.from_user.last_name +
      "\n" + "ID: " + str(message.chat.id) + "\n" + "Premium: " +
      str(message.from_user.is_premium) + "\n\n" + "Message: " + message.text,
    )
  except:
    bot.send_message(
      ID,
      "The error and user info: " + "\n\n" + "User name: @" +
      str(message.from_user.username) + "\n" + "Name: " +
      str(message.from_user.first_name) + "\n" + "ID: " +
      str(message.chat.id) + "\n" + "Premium: " +
      str(message.from_user.is_premium) + "\n\n" + "Message: " + message.text,
    )
  # print(message.text)
  print("Name: " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + "\tID: " + str(message.chat.id) + "\t\tMessage: " + str(message.text))

##############################################################################################################################

@bot.message_handler(commands=["help"])
def help(message):
  bot.reply_to(message, "Talk about your problem with @NXR81", reply_markup=markup)
  bot.send_message(message.chat.id,
                   "We will contact you as soon as possible")
  try:
    bot.send_message(
      ID,
      "The error and user info: " + "\n\n" + "User name: @" +
      str(message.from_user.username) + "\n" + "Name: " +
      str(message.from_user.first_name) + " " + message.from_user.last_name +
      "\n" + "ID: " + str(message.chat.id) + "\n" + "Premium: " +
      str(message.from_user.is_premium) + "\n\n" + "Message: " + message.text,
    )
  except:
    bot.send_message(
      ID,
      "The error and user info: " + "\n\n" + "User name: @" +
      str(message.from_user.username) + "\n" + "Name: " +
      str(message.from_user.first_name) + "\n" + "ID: " +
      str(message.chat.id) + "\n" + "Premium: " +
      str(message.from_user.is_premium) + "\n\n" + "Message: " + message.text,
    )
  print("Name: " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + "\tID: " + str(message.chat.id) + "\t\tMessage: " + str(message.text))

##############################################################################################################################

if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            time.sleep(15)
