import telegram

def mesajat(mesaj):
    """Direkt mesaj atar.

    :param mesaj: Str mesaj
    """
    # token
    Token = ''
    chat_id = 12345678
    bot = telegram.Bot(token=Token)
    bot.send_message(chat_id, text=mesaj)