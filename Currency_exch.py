from tkinter import *
import requests
# import json
# import pprint
from  tkinter import messagebox as mb
from tkinter import ttk


def update_base_label1(event):
    code = base_combobox1.get()
    name = curr[code]
    base_label1.config(text=name)


def update_base_label2(event):
    code = base_combobox2.get()
    name = curr[code]
    base_label2.config(text=name)


def update_target_label(event):
    code = target_combobox.get()
    name = curr[code]
    target_label.config(text=name)

def exchange1():
    global exchange_rate1, target_name, base_name1
    target_code = target_combobox.get()
    base_code1 = base_combobox1.get()
    if target_code and base_code1:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code1}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates']:
                exchange_rate1 = data['rates'][target_code]
                target_name = curr[target_code]
                base_name1 = curr[base_code1]
                # mb.showinfo("Курс обмена", f"Курс: {exchange_rate1:.2f} {target_name} за один {base_name1}")
            else:
                mb.showerror("Ошибка!", f"Валюта {target_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}!")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


def exchange2():
    global exchange_rate2, target_name, base_name2
    target_code = target_combobox.get()
    base_code2 = base_combobox2.get()
    if target_code and base_code2:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code2}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates']:
                exchange_rate2 = data['rates'][target_code]
                target_name = curr[target_code]
                base_name2 = curr[base_code2]
                # mb.showinfo("Курс обмена", f"Курс: {exchange_rate2:.2f} {target_name} за один {base_name2}")
            else:
                mb.showerror("Ошибка!", f"Валюта {target_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}!")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


def exchange():
    exchange1()
    exchange2()
    mb.showinfo("Курс обмена", f"Курс: {exchange_rate1:.2f} {target_name} за один {base_name1}\nКурс: {exchange_rate2:.2f} {target_name} за один {base_name2}")

curr = {
    "RUB": "Российский рубль",
    "USD": "Доллар США",
    "GBP": "Британский фунт стерлингов",
    "AED": "Дирхам ОАЭ",
    "AFN": "Афгани",
    "ALL": "Албанский лек",
    "AMD": "Армянский драм",
    "ANG": "Нидерландский антильский гульден",
    "AOA": "Ангольская кванза",
    "ARS": "Аргентинское песо",
    "AUD": "Австралийский доллар",
    "AWG": "Арубанский флорин",
    "AZN": "Азербайджанский манат",
    "BAM": "Конвертируемая марка Боснии и Герцеговины",
    "BBD": "Барбадосский доллар",
    "BDT": "Бангладешская така",
    "BGN": "Болгарский лев",
    "BHD": "Бахрейнский динар",
    "BIF": "Бурундийский франк",
    "BMD": "Бермудский доллар",
    "BND": "Брунейский доллар",
    "BOB": "Боливийский боливиано",
    "BRL": "Бразильский реал",
    "BSD": "Багамский доллар",
    "BTN": "Бутанский нгултрум",
    "BWP": "Ботсванская пула",
    "BYN": "Белорусский рубль",
    "BZD": "Белизский доллар",
    "CAD": "Канадский доллар",
    "CDF": "Конголезский франк",
    "CHF": "Швейцарский франк",
    "CLP": "Чилийское песо",
    "CNY": "Китайский юань",
    "COP": "Колумбийское песо",
    "CRC": "Костариканский колон",
    "CUP": "Кубинское песо",
    "CVE": "Эскудо Кабо-Верде",
    "CZK": "Чешская крона",
    "DJF": "Франк Джибути",
    "DKK": "Датская крона",
    "DOP": "Доминиканское песо",
    "DZD": "Алжирский динар",
    "EGP": "Египетский фунт",
    "ERN": "Эритрейская накфа",
    "ETB": "Эфиопский быр",
    "EUR": "Евро",
    "FJD": "Доллар Фиджи",
    "FKP": "Фунт Фолклендских островов",
    "FOK": "Фарерская крона",
    "GEL": "Грузинский лари",
    "GGP": "Фунт Гернси",
    "GHS": "Ганский седи",
    "GIP": "Гибралтарский фунт",
    "GMD": "Гамбийский даласи",
    "GNF": "Гвинейский франк",
    "GTQ": "Гватемальский кетсаль",
    "GYD": "Гайанский доллар",
    "HKD": "Гонконгский доллар",
    "HNL": "Гондурасская лемпира",
    "HRK": "Хорватская куна",
    "HTG": "Гаитянский гурд",
    "HUF": "Венгерский форинт",
    "IDR": "Индонезийская рупия",
    "ILS": "Израильский шекель",
    "IMP": "Фунт Острова Мэн",
    "INR": "Индийская рупия",
    "IQD": "Иракский динар",
    "IRR": "Иранский риал",
    "ISK": "Исландская крона",
    "JEP": "Фунт Джерси",
    "JMD": "Ямайский доллар",
    "JOD": "Иорданский динар",
    "JPY": "Японская иена",
    "KES": "Кенийский шиллинг",
    "KGS": "Киргизский сом",
    "KHR": "Камбоджийский риель",
    "KID": "Доллар Кирибати",
    "KMF": "Франк Комор",
    "KRW": "Южнокорейская вона",
    "KWD": "Кувейтский динар",
    "KYD": "Доллар Каймановых островов",
    "KZT": "Казахстанский тенге",
    "LAK": "Лаосский кип",
    "LBP": "Ливанский фунт",
    "LKR": "Шри-ланкийская рупия",
    "LRD": "Либерийский доллар",
    "LSL": "Лоти Лесото",
    "LYD": "Ливийский динар",
    "MAD": "Марокканский дирхам",
    "MDL": "Молдавский лей",
    "MGA": "Малагасийский ариари",
    "MKD": "Северомакедонский динар",
    "MMK": "Мьянманский кьят",
    "MNT": "Монгольский тугрик",
    "MOP": "Патака Макао",
    "MRU": "Мавританская угия",
    "MUR": "Маврикийская рупия",
    "MVR": "Мальдивская руфия",
    "MWK": "Малавийская квача",
    "MXN": "Мексиканское песо",
    "MYR": "Малайзийский ринггит",
    "MZN": "Мозамбикский метикал",
    "NAD": "Намибийский доллар",
    "NGN": "Нигерийская найра",
    "NIO": "Никарагуанская кордоба",
    "NOK": "Норвежская крона",
    "NPR": "Непальская рупия",
    "NZD": "Новозеландский доллар",
    "OMR": "Оманский риал",
    "PAB": "Панамский бальбоа",
    "PEN": "Перуанский соль",
    "PGK": "Кина Папуа-Новой Гвинеи",
    "PHP": "Филиппинское песо",
    "PKR": "Пакистанская рупия",
    "PLN": "Польский злотый",
    "PYG": "Парагвайский гуарани",
    "QAR": "Катарский риал",
    "RON": "Румынский лей",
    "RSD": "Сербский динар",
    "RWF": "Франк Руанды",
    "SAR": "Саудовский риал",
    "SBD": "Доллар Соломоновых островов",
    "SCR": "Сейшельская рупия",
    "SDG": "Суданский фунт",
    "SEK": "Шведская крона",
    "SGD": "Сингапурский доллар",
    "SHP": "Фунт Святой Елены",
    "SLE": "Леоне Сьерра-Леоне",
    "SLL": "Сьерра-леонский леоне",
    "SOS": "Сомалийский шиллинг",
    "SRD": "Суринамский доллар",
    "SSP": "Южносуданский фунт",
    "STN": "Добра Сан-Томе и Принсипи",
    "SYP": "Сирийский фунт",
    "SZL": "Свазилендский лилангени",
    "THB": "Тайский бат",
    "TJS": "Таджикский сомони",
    "TMT": "Туркменский манат",
    "TND": "Тунисский динар",
    "TOP": "Паанга Тонга",
    "TRY": "Турецкая лира",
    "TTD": "Доллар Тринидада и Тобаго",
    "TVD": "Доллар Тувалу",
    "TWD": "Тайваньский доллар",
    "TZS": "Танзанийский шиллинг",
    "UAH": "Украинская гривна",
    "UGX": "Угандийский шиллинг",
    "UYU": "Уругвайское песо",
    "UZS": "Узбекский сум",
    "VES": "Венесуэльский боливар",
    "VND": "Вьетнамский донг",
    "VUV": "Вату Вануату",
    "WST": "Тала Самоа",
    "XAF": "Франк КФА BEAC",
    "XCD": "Восточно-карибский доллар",
    "XDR": "СПЗ (Специальные права заимствования)",
    "XOF": "Франк КФА BCEAO",
    "XPF": "Французский тихоокеанский франк",
    "YER": "Йеменский риал",
    "ZAR": "Южноафриканский рэнд",
    "ZMW": "Замбийская квача",
    "ZWL": "Зимбабвийский доллар"
}

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x450")

label1 = (Label(text="Базовая валюта"))
label1.pack(padx=10, pady=10)
base_combobox1 = ttk.Combobox(values=list(curr.keys()))
base_combobox1.pack(padx=10, pady=10)
base_combobox1.bind("<<ComboboxSelected>>", update_base_label1)
base_label1 = ttk.Label()
base_label1.pack(padx=10, pady=10)

label2 = (Label(text="Вторая базовая валюта"))
label2.pack(padx=10, pady=10)
base_combobox2 = ttk.Combobox(values=list(curr.keys()))
base_combobox2.pack(padx=10, pady=10)
base_combobox2.bind("<<ComboboxSelected>>", update_base_label2)
base_label2 = ttk.Label()
base_label2.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)

target_combobox = ttk.Combobox(values=list(curr.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

target_label = ttk.Label()
target_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
