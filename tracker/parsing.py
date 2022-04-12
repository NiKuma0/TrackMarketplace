from urllib.request import urlopen
from lxml import etree


xpaths = {
    'title': '//*[@id="container"]/div[2]/div/div[2]/h1/span[2]',
    'brand': '//*[@id="container"]/div[2]/div/div[2]/h1/span[1]',
    'price': '//*[@id="infoBlockProductCard"]/div[2]/div/div/p/span',
    'old_price': '//*[@id="infoBlockProductCard"]/div[2]/div/div/p/del',
}


def parsing(card_id: int | str):
    url = f'https://www.wildberries.ru/catalog/{card_id}/detail.aspx'
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree: etree._ElementTree = etree.parse(response, htmlparser)
    data = {
        'title': tree.xpath(xpaths['title'])[0].text,
        'brand': tree.xpath(xpaths['brand'])[0].text,
    }
    price = tree.xpath(xpaths['price'])[0].text.split()
    old_price = tree.xpath(xpaths['old_price'])
    if not old_price:
        old_price = price
    else:
        old_price = old_price[0].text.split()
    data['price'] = int(''.join(price[:-1]))
    data['old_price'] = int(''.join(old_price[:-1]))
    return data
