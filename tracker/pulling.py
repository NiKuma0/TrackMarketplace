import requests
import datetime
from urllib.error import HTTPError
from urllib.request import urlopen
from lxml import etree
from apscheduler.schedulers.background import BackgroundScheduler

from tracker.models import Tracker, Card


_xpaths = {
    'title': '//*[@id="container"]/div[2]/div/div[2]/h1/span[2]',
    'brand': '//*[@id="container"]/div[2]/div/div[2]/h1/span[1]',
    'price': '//*[@id="infoBlockProductCard"]/div[2]/div/div/p/span',
    'old_price': '//*[@id="infoBlockProductCard"]/div[2]/div/div/p/del',
}
_deltas = {
    '1 hours': datetime.timedelta(hours=1),
    '12 hours': datetime.timedelta(hours=12),
    '24 hours': datetime.timedelta(hours=24),
}


def parsing(card_id: int | str):
    url = f'https://www.wildberries.ru/catalog/{card_id}/detail.aspx'
    requests.get(url).raise_for_status()
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree: etree._ElementTree = etree.parse(response, htmlparser)
    data = {
        'title': tree.xpath(_xpaths['title'])[0].text,
        'brand': tree.xpath(_xpaths['brand'])[0].text,
    }
    price = tree.xpath(_xpaths['price'])[0].text.split()
    old_price = tree.xpath(_xpaths['old_price'])
    if not old_price:
        old_price = price
    else:
        old_price = old_price[0].text.split()
    data['price'] = int(''.join(price[:-1]))
    data['old_price'] = int(''.join(old_price[:-1]))
    return data


def _check_interval(tracker: Tracker) -> bool:
    if not tracker.history.exists():
        return True
    step = _deltas[tracker.step]
    date_step = datetime.datetime.now() - step
    last_check = tracker.history.first().date.timestamp()
    return last_check <= date_step.timestamp()


def get_updates():
    """
    Создаёт новые карточки для трекера через подходящий интервал 
    """
    now = datetime.date.today()
    trackers: list[Tracker] = Tracker.objects.all().filter(
        start_check__lte=now, end_check__gte=now
    )
    for tracker in trackers:
        if not _check_interval(tracker):
            continue
        try:
            card_data = parsing(tracker.article)
        except HTTPError:
            continue
        Card.objects.create(
            tracker=tracker,
            **card_data,
        )


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        get_updates,
        'interval',
        hours=1
    )
    scheduler.start()
