from scrapers.lamoda_scrapper import LamodaScrapper
from scrapers.farfetch_scrapper import FarfetchScrapper
from scrapers.asos_scrapper import AsosScrapper
from scrapers.stockmann_scrapper import StockmannScrapper


LAMODA_BASE_URL = 'https://www.lamoda.ru'
LAMODA_ITEMS_URL = '{}/c/563/bags-sumki-chehli'.format(LAMODA_BASE_URL)
LAMODA_IS_SALE = 1
LAMODA_BRANDS = '1123%2C25633%2C1733%2C4869%2C1861%2C27081%2C6477%2C5584%2C23219%2C1841%2C1887%2C23839%2C2829%2C6091' \
                '%2C4355%2C3795%2C32138%2C25812%2C5112%2C24641%2C4489%2C6180%2C26934%2C573%2C6202%2C4607%2C29528' \
                '%2C18559%2C25690 '

FARFETCH_BASE_URL = 'https://www.farfetch.com'
FARFETCH_ITEMS_URL = '{}/ru/shopping/women/bags-purses-1/items.aspx'.format(FARFETCH_BASE_URL)
FARFETCH_DISCOUNT = '0-30|30-50|50-60|60-100'
FARFETCH_SORT = '5'
FARFETCH_PAGE_LIMIT = 30

ASOS_BASE_URL = 'https://www.asos.com/ru'
ASOS_ITEMS_URL = '{}/women/rasprodazha/aksessuary/cat/?cid=1929&nlid=%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D0%B4%D0%B0' \
                '%D0%B6%D0%B0%7C%D0%B0%D0%BA%D1%81%D0%B5%D1%81%D1%81%D1%83%D0%B0%D1%80%D1%8B&refine' \
                '=attribute_1047:8283'.format(ASOS_BASE_URL)

STOCKMANN_BASE_URL = 'https://stockmann.ru'
STOCKMANN_ITEMS_URL = '{}/category/222-zhenskie-sumki'.format(STOCKMANN_BASE_URL)


# BRANDS = ['love moschino']
# BRANDS = ['karl lagerfeld']
BRANDS = []

if __name__ == '__main__':
    print('Started')

    items_on_sale = []

    lamoda_scrapper = LamodaScrapper(LAMODA_BASE_URL, LAMODA_ITEMS_URL, LAMODA_BRANDS, LAMODA_IS_SALE)
    lamoda_items_on_sale = lamoda_scrapper.parse()
    items_on_sale.extend(lamoda_items_on_sale)

    farfetch_scrapper = FarfetchScrapper(FARFETCH_BASE_URL, FARFETCH_ITEMS_URL, FARFETCH_DISCOUNT,
                                         FARFETCH_SORT, FARFETCH_PAGE_LIMIT)
    farfetch_items_on_sale = farfetch_scrapper.parse()
    items_on_sale.extend(farfetch_items_on_sale)

    asos_scrapper = AsosScrapper(ASOS_BASE_URL, ASOS_ITEMS_URL)
    asos_items_on_sale = asos_scrapper.parse()
    items_on_sale.extend(asos_items_on_sale)

    stockmann_scrapper = StockmannScrapper(STOCKMANN_BASE_URL, STOCKMANN_ITEMS_URL)
    stockmann_items_on_sale = stockmann_scrapper.parse()
    items_on_sale.extend(stockmann_items_on_sale)

    if BRANDS:
        items_on_sale = list(filter(lambda x: any([b in x['name'].lower() for b in BRANDS]), items_on_sale))

    items_on_sale.sort(key=lambda x: 1 - x['price'] / x['old_price'], reverse=True)

    for item in items_on_sale[:1000]:
        print(item)
