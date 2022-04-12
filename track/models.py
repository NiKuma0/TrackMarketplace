from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Track(models.Model):
    class TimeStepChoice(models.TextChoices):
        ONE_HOUR = '1h', 'Один час'
        TWELVE_HOURS = '12h', 'Двенадцать часов'
        TWENTY_FOUR_HOURS = '24h', 'Двадцать часов'

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
        related_name='tracks',
    )


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
    track = models.ForeignKey(
        Track,
        related_name='history',
        on_delete=models.PROTECT
    )
