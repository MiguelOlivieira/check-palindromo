#importa a função normalize do módulo unicodedata
from unicodedata import normalize


palavra = input("Digite uma palavra: ")

#Faz a conversão, removendo os acentos e convertendo para minusculo.
conversao = normalize('NFKD', palavra.lower()).encode('ASCII','ignore').decode('ASCII')
print(conversao)

#remove os espaços em branco
conversao = ''.join(x for x in conversao if x.isalnum())

#verificação do palindromo
print('É um palíndromo') if conversao[::-1] == conversao else print('Não é um palíndromo')

