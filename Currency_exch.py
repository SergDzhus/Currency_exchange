from tkinter import *
import requests
# import json
# import pprint
from  tkinter import messagebox as mb
from tkinter import ttk


def update_currency_label(event):
    code = combobox.get()
    name = curr[code]
    currency_label.config(text=name)

def exchange():
    # code_0 = entry.get()
    # code = code_0.upper()
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = curr[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {currency_name} за один доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}!")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")

curr = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт',
    'CHF': 'Швейцарский франк',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар'
}

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)
combobox = ttk.Combobox(values=list(curr.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к USD", command=exchange).pack(padx=10, pady=10)

window.mainloop()
