import requests
import bs4
from unidecode import unidecode
from termcolor import colored


#request web and get data with selector
res = requests.get('https://arzdigital.com/coins/')
soup = bs4.BeautifulSoup(res.content, features='html.parser')
coins_price = soup.select('.arz-sort-value :nth-child(1) span')

#client
Client_response = input('\nEnter you coins like Bitcoin\n')
print('\n')

#loop for check coin and get data
for coins_p in coins_price:
    if Client_response.strip().title() in coins_p.text:     #check coins in list
        print(colored(f'{coins_p.text}: ', 'green'))                                #so print it
        price_index = coins_price.index(coins_p) + 1        #in this list price coins is index coin in list + 1 we got index of price
        price = coins_price[price_index]                    #and got the value of price index
        price = unidecode(price.text)                       #unidecode to change persian number to eng number
        print(f'price is {price} toman\n')
    else:
        print(colored('you selected coins not here or you spell is not correctly', 'red'))
        break
