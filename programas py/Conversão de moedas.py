from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import os
import re
import time
from tkinter import *
from tkinter import messagebox

url = 'https://www.infomoney.com.br/cotacoes/cambio/moeda/dolar/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'}
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.text, 'html.parser')
g = soup.find('div', class_='value').text
valor = re.search(r'\d+,\d+', g).group()

real = 0
dolar = 0

janela = Tk()
janela.title("Calculadora de conversão de moedas")
janela.geometry("400x160")
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)

realtask = Label(janela, text="Digite o valor em reais:")
realtask.grid (column=0, row=1)
camporealtask = Entry(janela)
camporealtask.grid (column=1, row=1)

dolartask = Label(janela, text="Digite o valor em dolar:")
dolartask.grid (column=0, row=4)
campodolartask = Entry(janela)
campodolartask.grid (column=1, row=4)

dolartask = Label(janela, text="  ")
dolartask.grid (column=0, row=2)
dolartask = Label(janela, text="  ")
dolartask.grid (column=0, row=3)
dolartask = Label(janela, text="  ")
dolartask.grid (column=0, row=0)
dolartask = Label(janela, text="  ")
dolartask.grid (column=0, row=5)

def getInput () :
    valor_real = camporealtask.get().strip()
    valor_dolar = campodolartask.get().strip()

    if valor_real =='' and valor_dolar == '':
         messagebox.showinfo("Erro!","Erro! Digite um valor para conversão.")

    elif valor_dolar == '':
         valor_dolar = 0
         valorParaD = float(valor_real) / float(valor.replace(',', '.'))
         valorParaD = round(valorParaD, 2)
         messagebox.showinfo("Valor do convertido", f"{valor_real} BRL quivale a {valorParaD} USD após conversão.\n\n1 USD = {float(valor.replace(',', '.'))} BRL")
    elif valor_real == '':
         valor_real = 0
         valorParaR = float(valor_dolar) * float(valor.replace(',', '.'))
         valorParaR = round(valorParaR, 2)
         messagebox.showinfo("Valor do convertido", f"{valor_dolar} USD equivale a {float(valorParaR)} BRL após conversão.\n\n1 USD = {float(valor.replace(',', '.'))} BRL")
    elif valor_real and valor_dolar:
        valorParaD = float(valor_real) / float(valor.replace(',', '.'))
        valorParaD = round(valorParaD, 2)
        valorParaR = float(valor_dolar) * float(valor.replace(',', '.'))
        valorParaR = round(valorParaR, 2)
        messagebox.showinfo("Valor do convertido", f"{valor_real} BRL quivale a {valorParaD} USD\n{valor_dolar} USD equivale a {valorParaR} BRL.\n\n1 USD = {float(valor.replace(',', '.'))} BRL")
    return

convert = Button(janela, text="Converter", command=getInput)
convert.grid(column=1, row=6)

janela.mainloop()