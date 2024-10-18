from tkinter import *
import requests
import json
import pprint
from  tkinter import messagebox as mb


def exchange():

result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x80")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к USD", command=exchange).pack(padx=10, pady=10)

window.mainloop()
