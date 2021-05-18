import requests

API_CURRENCY_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


def main():
    print('Start Holden Poker')
    response = requests.get(API_CURRENCY_URL)
    price = input('Please write UAH count: ')
    currency_list = response.json()
    for currency in currency_list:
        if currency['ccy'] == "USD":
            print('{} to {}. Buy {}. Sale {}'.format(
                currency['base_ccy'],
                currency['ccy'],
                currency['buy'],
                currency['sale'],
            ))
            print(int(price) / float(currency['buy']))

if __name__ == '__main__':
    main()
