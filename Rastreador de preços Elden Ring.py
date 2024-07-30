#Importa a biblioteca requests e a biblioteca Beautiul Soup
import requests
from bs4 import BeautifulSoup

#Armazena a URL na variável URL
url = 'https://www.xbox.com/pt-BR/games/store/elden-ring/9P3J32CTXLRZ/0010'

#Armazena a request para o site na variável request
req = requests.get(url)

#Cria o objeto BeatifulSoup
soup = BeautifulSoup(req.text, "lxml")

#Armazena o preço em uma variável
preco = soup.select(".Price-module__boldText___1i2Li.Price-module__moreText___sNMVr")[0].text

#Editando o texto para aparecer somente o número
preco = preco.replace(",", ".")
preco = preco[2:8]
preco = float(preco)
print(preco)

#Definindo o preço mínimo para compra
meupreco = 200

#Cria a condição para verificar se está dentro do que pretendo pagar
if preco <= meupreco:
    print(f'Preço menor de R$200.00 (R${preco})')
else:
    print(f'Preço maior que R$200.00 (R${preco})')