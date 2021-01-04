import requests
from bs4 import BeautifulSoup

class BTC:

    usd_price = -1

    @classmethod
    def UpdatePrice(cls):
        r = requests.get('https://www.coinbase.com/price/bitcoin')

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            dollars = soup.select_one('span[class*="AssetChartAmount__Number"]').getText()
            cents = soup.select('span[class*="AssetChartAmount__AmountSuper"]')[1].getText()
            cls.usd_price = (dollars + cents).replace(',', '')
        else:
            print("There was a problem updating the price")

if __name__ == "__main__":
    print(BTC.usd_price)
    BTC.UpdatePrice()
    print(BTC.usd_price)