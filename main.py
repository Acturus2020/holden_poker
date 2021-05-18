import requests
import publicip

API_CURRENCY_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
IP_ADDRESS_URL = "http://ip-api.com/json/"

def get_user_address(ip_address):
    url = IP_ADDRESS_URL.format(ip_address)
    response = requests.get(url)
    user_address = response.json()
    print('user_address: ', user_address)


def main():
    get_user_address(publicip.get())
    print('Start Holden Poker')
    response = requests.get(API_CURRENCY_URL)
    currency_list = response.json()
    for currency in currency_list:
        print('{} to {}. Buy {}. Sale {}'.format(
            currency['base_ccy'],
            currency['ccy'],
            currency['buy'],
            currency['sale'],
        ))

if __name__ == '__main__':
    main()