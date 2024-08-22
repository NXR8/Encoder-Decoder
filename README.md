# Telegram Encryption Bot

This Telegram bot performs encryption and decryption of messages using a custom encoding scheme. It also handles basic commands and provides error reporting.

## Overview

The bot supports the following commands:
- **/ny**: Encrypts the provided text or replies to a message.
- **/text**: Decrypts the provided text or replies to a message.
- **/start**: Provides a brief introduction and example usage.
- **/help**: Provides help and directs users to contact support.

## Code Explanation

### Imports

```python
import time
import telebot, base64
from telebot import types
import logging
```
- **time**: Used for introducing delays in case of errors.
- **telebot**: The library used to interact with the Telegram API.
- **base64**: Used for encoding and decoding messages.
- **logging**: Used for logging errors.

### Encoding and Decoding

```python
encoded = {
  "0": ".$.0", "1": "/@]5", "2": ".#(7", ...
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
```
- **encoded** and **decoded**: Dictionaries for encoding and decoding characters.
- **encode**: Lambda function to encode text using the `encoded` dictionary and base64 encoding.
- **decode**: Function to decode the text by reversing the encoding process.

### Bot Configuration

```python
token = "<your_telegram_bot_token>"
bot = telebot.TeleBot(token)
ID = <your_ID>
```
- **token**: Replace `<your_telegram_bot_token>` with your actual Telegram bot token.
- **ID**: Replace `<your_ID>` with your Telegram user ID for error reporting.

### Command Handlers

- **/ny**: Encrypts the message or the reply to a message.
- **/text**: Decrypts the message or the reply to a message.
- **/start**: Sends a welcome message and usage examples.
- **/help**: Provides contact information for support.

### Example Command Handlers

#### Encrypt Message

```python
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
    # Error handling
    ...
```

#### Decrypt Message

```python
@bot.message_handler(commands=["text"])
def toText(message):
  try:
    msg = message.text
    msg = msg.replace("/text", "").strip()
    if message.reply_to_message:
        replied_message = message.reply_to_message.text
        msg = decode(replied_message)
    else:
        text_message = message.text.replace("/text", "").strip()
        msg = decode(text_message)
    bot.reply_to(message, msg, reply_markup=markup)
  except:
    # Error handling
    ...
```

### Running the Bot

To run the bot, execute the script:

```bash
python ENCODING_BOT.py
```

The bot will start and listen for incoming messages.

## Error Handling

The bot logs errors and sends error reports to the specified Telegram user ID. If an error occurs, it will try to handle it gracefully and log the relevant information.

## License

This project is licensed under the MIT License.

## Contact

For support or inquiries, contact [@NXR81](https://t.me/NXR81) or [@O0O0I](https://t.me/O0O0I) on Telegram.

To try out the bot, visit the following link: [NY_Encoding_bot](https://t.me/NY_Encoding_bot)
