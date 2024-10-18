from tkinter import *
import requests
# import json
# import pprint
from  tkinter import messagebox as mb
from tkinter import ttk


def update_currency_label(event):
    code = target_combobox.get()
    name = curr[code]
    currency_label.config(text=name)

def exchange():
    # code_0 = entry.get()
    # code = code_0.upper()
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                target_name = curr[target_code]
                base_name = curr[base_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {target_name} за один {base_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {target_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}!")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")

curr = {
    'RUB': 'Российский рубль',
    'USD': 'Американский доллар',
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
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)

base_combobox = ttk.Combobox(values=list(curr.keys()))
base_combobox.pack(padx=10, pady=10)
# base_combobox.bind("<<ComboboxSelected>>", update_currency_label)

Label(text="Целевая валюта").pack(padx=10, pady=10)

target_combobox = ttk.Combobox(values=list(curr.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
