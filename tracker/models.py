from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tracker(models.Model):
    class TimeStepChoice(models.TextChoices):
        ONE_HOUR = '1h', 'Один час'
        TWELVE_HOURS = '12h', 'Двенадцать часов'
        TWENTY_FOUR_HOURS = '24h', 'Двадцать четыре часа'

    article = models.IntegerField(
        'Артикул',
    )
    start_check = models.DateTimeField(
        verbose_name='Начало периуда'
    )
    end_check = models.DateTimeField(
        verbose_name='Конец периода'
    )
    step = models.CharField(
        max_length=255,
        verbose_name='Интервал',
        choices=TimeStepChoice.choices
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='trackers',
    )

    class Meta:
        verbose_name = 'Трекер'
        verbose_name_plural = 'Трекеры'


class Card(models.Model):
    title = models.CharField(
        'Названия товара',
        max_length=400,
    )
    brand = models.CharField(
        'Бренд',
        max_length=400,
    )
    price = models.IntegerField(
        'Цена'
    )
    old_price = models.IntegerField(
        'Цена без скидки'
    )
    date = models.DateTimeField(auto_now=True)
    tracker = models.ForeignKey(
        Tracker,
        related_name='history',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        orderring = ('date',)
