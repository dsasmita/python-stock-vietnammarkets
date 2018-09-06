import bs4
import requests


class VietnamMarkets:
    HEADERS = {
        'Accept-Encoding': 'gzip, '
        'deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0', 'Connection': 'keep-alive'}
    LINK = 'http://stock.vietnammarkets.com/vietnam-stock-market.php'

    def company_index(self):
        content = requests.get(VietnamMarkets.LINK, timeout=10, headers=VietnamMarkets.HEADERS)
        bs = bs4.BeautifulSoup(content.text, "html.parser")

        result = bs.find('div', 'results')

        companies = []
        if result != None:
            for list in result.select("tr"):
                row = list.findAll('td')
                if row[0].getText() != 'Ticker':
                    tmp = {}
                    tmp['ticker_symbol'] = row[0].getText()
                    tmp['url'] = row[0].find('a')['href']
                    tmp['company_name'] = row[1].getText()
                    tmp['business'] = row[2].getText()
                    tmp['listing_bourse'] = row[3].getText()
                    companies.append(tmp)

        return companies