import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# DADOS DO BOT
TOKEN = '7854280182:AAHohxQ0xbeKoXKgEzHrJSd5diKiOjm-IuY'
CHAT_ID = '7833489050'

# PALAVRAS-CHAVE
palavras_chave = ["brazil", "brasil", "china", "eua", "commodities"]

# FUNÇÃO PARA ENVIAR MENSAGEM PARA O TELEGRAM
def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=payload)

# FUNÇÃO PARA CAPTURAR NOTÍCIAS DO TRADING ECONOMICS
def capturar_noticias_tradingeconomics():
    url = "https://tradingeconomics.com/stream"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    noticias = []
    for item in soup.find_all("a"):
        texto = item.get_text(strip=True)
        if texto and any(palavra in texto.lower() for palavra in palavras_chave):
            noticias.append(texto)
    return noticias

# LOOP AUTOMÁTICO CADA 15 MIN DAS 07H ÀS 19H (horário de Brasília)
while True:
    agora = datetime.utcnow() + timedelta(hours=-3)
    hora = agora.hour
    minuto = agora.minute

    if 7 <= hora <= 19 and minuto % 15 == 0:
        noticias = capturar_noticias_tradingeconomics()
        if noticias:
            mensagem = "\n".join(noticias)
            enviar_telegram(mensagem)
        time.sleep(60)  # evita enviar repetido no mesmo minuto

    time.sleep(30)
