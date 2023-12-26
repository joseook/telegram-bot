**README.md - Telegram Bot Project**

# Telegram Bot for Order Management

This Telegram bot allows users to place new orders, request refunds, and add new ingredients to their orders. The bot is built using the Telebot library and employs a state machine to collect information from users in a structured manner.

## Getting Started

To run the bot, you need to obtain a Telegram Bot API key. Follow these steps:

1. Create a new bot on Telegram by talking to [@BotFather](https://t.me/BotFather).
2. Follow the instructions to create a new bot and obtain the API key.

Once you have the API key, replace the placeholder in the script with your actual key:

```python
KEY_API = "Your-Telegram-Bot-API-Key"
```

### Prerequisites

- Python 3
- Telebot library (install using `pip install pyTelegramBotAPI`)

### Installing

1. Clone the repository:

```bash
git clone https://github.com/joseook/telegram-bot.git
cd telegram-bot
```


2. Replace the `KEY_API` placeholder with your Telegram Bot API key.

```python
KEY_API = "Your-Telegram-Bot-API-Key"
```

## Features

1. **Start Command (/start):**
   - Welcomes users and provides a menu of available options.
   - Options include placing a new order (/Pedido), requesting a refund (/Reembolso), and adding a new ingredient to the order (/Adicionar).

2. **Pedido Command (/Pedido):**
   - Initiates the order process by prompting users for order details.
   - Utilizes a state machine to collect information step by step (product, quantity, address).
   - Displays a summary of the order once all information is collected.

3. **Reembolso Command (/Reembolso):**
   - Placeholder for processing refund requests.
   - Users are prompted to provide details about the refund request.

4. **Adicionar Command (/Adicionar):**
   - Informs users to add new products through the website or contact a specified phone number.

## Usage

1. Start the bot by running the script:

```bash
python main.py
```

2. Interact with the bot on Telegram. Use the /start command to initiate the conversation.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and suggestions are valuable.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- The Telebot library for simplifying the development of Telegram bots.
- Inspiration from real-world order management systems.

---
