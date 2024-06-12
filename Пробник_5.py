import tkinter as tk
import requests


def get_currency_rate(currency_code):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    print(data)
    currency_name = data['Valute'][currency_code]['Name']
    currency_rate = data['Valute'][currency_code]['Value']

    return currency_name, currency_rate


def show_currency_rate():

    currency_code = entry.get()
    currency_name, currency_rate = get_currency_rate(currency_code)

    result_window = tk.Toplevel(root)
    result_window.title('Курс валют')
    result_window.geometry('250x150')
    result_window.iconbitmap('10147259.ico')

    result_label = tk.Label(result_window, text=f'{currency_name}: {round(currency_rate, 2)}')
    result_label.pack()


root = tk.Tk()
root.title('Курс валют')
root.geometry("400x400")
root.iconbitmap('10147259.ico')

entry_label = tk.Label(root, text='Введите аббревиатуру (например, USD)')
entry_label.pack()

entry = tk.Entry(root)
entry.pack(pady=10)
entry.focus()

show_button = tk.Button(root, text='Курс валют', command=show_currency_rate)
show_button.pack()



def show_currency_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()

    currencies = data['Valute']

    currency_list_window = tk.Toplevel(root)
    currency_list_window.title('Справочник')
    currency_list_window.iconbitmap('book.ico')
    scrollbar = tk.Scrollbar(currency_list_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    currency_text = tk.Text(currency_list_window, yscrollcommand=scrollbar.set)
    currency_text.pack(fill=tk.BOTH, expand=True)
    for currency_code, currency_data in currencies.items():
        currency_name = currency_data['Name']
        currency_text.insert(tk.END, f'{currency_code}-{currency_name}\n')
        scrollbar.config(command=currency_text.yview)


show_currency_list_button = tk.Button(root, text='Справочник валют', command=show_currency_list)
show_currency_list_button.pack(pady=10)

root.mainloop()


