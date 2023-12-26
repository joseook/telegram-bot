import telebot

KEY_API = "Adicione aqui a key api do telegram bot"

bot = telebot.TeleBot(KEY_API)

# Dicionário para armazenar informações do usuário
user_data = {}

# Estados da máquina de estado
STATE_IDLE = "idle"
STATE_WAITING_FOR_ORDER = "waiting_for_order"
STATE_WAITING_FOR_QUANTITY = "waiting_for_quantity"
STATE_WAITING_FOR_ADDRESS = "waiting_for_address"

# Comando para iniciar a conversa
@bot.message_handler(commands=["start"])
def start(message):
    texto = """
        Olá, seja bem-vindo(a) à nossa conversa. Como posso ajudar você hoje?
        Escolha uma das opções abaixo:
            /Pedido - Fazer um novo pedido;
            /Reembolso - Solicitar reembolso;
            /Adicionar - Adicionar um novo ingrediente ao pedido.

        Digitar/Escrever qualquer outra coisa no chat não funcionará, então escolha uma das opções acima clicando.
    """
    bot.reply_to(message, texto)

# Comando para lidar com pedidos
@bot.message_handler(commands=["Pedido"])
def pedido(message):
    # Iniciar a máquina de estado para coletar informações do pedido
    user_data[message.chat.id] = {"state": STATE_WAITING_FOR_ORDER, "order_details": {}}
    bot.send_message(message.chat.id, "Por favor, forneça os detalhes do seu pedido.")

# Comando para lidar com solicitações de reembolso
@bot.message_handler(commands=["Reembolso"])
def reembolso(message):
    # Implemente a lógica para processar solicitações de reembolso
    bot.send_message(message.chat.id, "Por favor, forneça detalhes sobre a solicitação de reembolso.")

# Comando para adicionar ingredientes
@bot.message_handler(commands=["Adicionar"])
def adicion(message):
    bot.send_message(message.chat.id, "Para adicionar um novo produto, acesse nosso site: [Link do Site] ou telefone para: 82 9999-9999")

# Lidar com mensagens no estado de coleta de informações do pedido
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("state") == STATE_WAITING_FOR_ORDER)
def handle_order(message):
    user_data[message.chat.id]["order_details"]["produto"] = message.text
    user_data[message.chat.id]["state"] = STATE_WAITING_FOR_QUANTITY
    bot.send_message(message.chat.id, "Ótimo! Agora, por favor, informe a quantidade desejada.")

# Lidar com mensagens no estado de coleta de quantidade do pedido
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("state") == STATE_WAITING_FOR_QUANTITY)
def handle_quantity(message):
    try:
        quantidade = int(message.text)
        user_data[message.chat.id]["order_details"]["quantidade"] = quantidade
        user_data[message.chat.id]["state"] = STATE_WAITING_FOR_ADDRESS
        bot.send_message(message.chat.id, "Entendido! Agora, por favor, informe o endereço de entrega.")
    except ValueError:
        bot.send_message(message.chat.id, "Por favor, forneça uma quantidade válida.")

# Lidar com mensagens no estado de coleta de endereço
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("state") == STATE_WAITING_FOR_ADDRESS)
def handle_address(message):
    user_data[message.chat.id]["order_details"]["endereco"] = message.text
    # Agora você tem todas as informações do pedido, pode processar ou armazenar conforme necessário
    order_details = user_data[message.chat.id]["order_details"]
    bot.send_message(message.chat.id, f"Pedido recebido!\n\nDetalhes do Pedido:\nProduto: {order_details['produto']}\nQuantidade: {order_details['quantidade']}\nEndereço: {order_details['endereco']}")
    # Reiniciar o estado
    user_data[message.chat.id]["state"] = STATE_IDLE

# Melhoria na mensagem padrão
@bot.message_handler(func=lambda message: True)
def respond(message):
    texto = """
        Olá, seja bem-vindo(a) à nossa conversa. Como posso ajudar você hoje?
        Escolha uma das opções abaixo:
            /Pedido - Fazer um novo pedido;
            /Reembolso - Solicitar reembolso;
            /Adicionar - Adicionar um novo ingrediente ao pedido.

        Digitar/Escrever qualquer outra coisa no chat não funcionará, então escolha uma das opções acima clicando.
    """
    bot.reply_to(message, texto)

# Tratamento de erros
@bot.message_handler(func=lambda message: True)
def handle_errors(message):
    try:
        def ajuda(message):
            bot.send_message(message.chat.id, "Esta é a mensagem de ajuda.")

    except Exception as e:
        bot.send_message(message.chat.id, f"Desculpe, ocorreu um erro: {str(e)}")

# Iniciar o bot
bot.polling()
