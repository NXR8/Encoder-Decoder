## README.md

### Overview

This project is a Telegram bot built using the `telebot` library. The bot offers multiple functionalities, including encoding and decoding text with a custom cipher, handling basic bot commands, and fetching the external IP address of the server hosting the bot.

### Features

1. **Text Encoding (`/ny`)**: 
   - Encodes a message or a reply to a message using a custom encoding scheme.
   
2. **Text Decoding (`/text`)**: 
   - Decodes a previously encoded message back to its original form.

5. **Help Command (`/help`)**: 
   - Directs users to contact the bot developer for support.

6. **Start Command (`/start`)**: 
   - Welcomes new users and provides instructions on how to use the bot.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NXR8/encoder-decoder
   cd encoder-decoder
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then install the required libraries:
   ```bash
   pip install pyTelegramBotAPI requests
   ```

3. **Set up the bot token:**
   Replace the placeholder `token` in the code with your own Telegram bot token.

4. **Run the bot:**
   Start the bot by executing the script:
   ```bash
   python ENCODING_BOT.py
   ```

### Configuration

- **Telegram Bot Token**: 
  - The bot token should be set in the `token` variable.
  
- **Admin User ID**: 
  - Set the `ID` to the Telegram user ID of the bot's administrator to receive error reports and certain commands.

### Usage

- **Encoding a Message:**
  - Send `/ny <your_message>` to the bot, and it will return the encoded version.
  
- **Decoding a Message:**
  - Send `/text <encoded_message>` to the bot, and it will return the decoded version.
  
### Error Handling

- The bot handles errors by sending a message to the admin user with details about the error and the user who triggered it.
  
- If the bot encounters an issue during its execution, it logs the error and retries the operation after a delay.

### Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project.

### License

This project is licensed under the MIT License. 

### Contact

For any inquiries or support, please contact [@NXR81](https://t.me/NXR81) or [@O0O0I](https://t.me/O0O0I) on Telegram.
