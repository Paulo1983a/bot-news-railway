import requests
import time
from datetime import datetime, timedelta

# DADOS DO BOT
TOKEN = '7854280182:AAHohxQ0xbeKoXKgEzHrJSd5diKiOjm-IuY'
CHAT_ID = '7833489050'

# PALAVRAS-CHAVE
palavras_chave = ["Brazil", "Brasil", "China", "EUA", "commodities"]

# FUNÇÃO PARA ENVIAR MENSAGEM
def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=payload)

# FUNÇÃO DE NOTÍCIAS (placeholder para teste)
def capturar_noticias():
    noticias = []
    for palavra in palavras_chave:
        noticias.append(f"Alerta de notícia relevante: {palavra}")
    return noticias

# EXECUTA APENAS ÀS 19:00 (horário de Brasília)
while True:
    agora = datetime.utcnow() + timedelta(hours=-3)
    hora = agora.hour
    minuto = agora.minute

    if hora == 19 and minuto == 0:
        noticias = capturar_noticias()
        if noticias:
            mensagem = "\n".join(noticias)
            enviar_telegram(mensagem)
        time.sleep(60)  # evita repetição no mesmo minuto

    time.sleep(30)
