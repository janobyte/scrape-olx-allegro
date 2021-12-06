from bs4 import BeautifulSoup
import requests


class UserQuery:
    """
    to get initial scraping url from users
    """
    def __init__(self):
        self.query = input('Input your query: ')
    def query2url(self):
        qinput = self.query.replace(' ', '-')
        self.query = f'https://www.olx.pl/oferty/q-{qinput}/'
        return self.query


userqinput = UserQuery()
userqinput.query2url()

print(userqinput.query)

r = requests.get(f"{userqinput.query}", headers={
                 'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content