import requests

API_CURRENCY_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


def main():
    print('Start Holden Poker')
    response = requests.get(API_CURRENCY_URL)
    print(response.json())

if __name__ == '__main__':
    main()