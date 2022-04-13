from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tracker(models.Model):
    class TimeStepChoice(models.TextChoices):
        ONE_HOUR = '1 hours', 'Один час'
        TWELVE_HOURS = '12 hours', 'Двенадцать часов'
        TWENTY_FOUR_HOURS = '24 hours', 'Двадцать четыре часа'

    article = models.IntegerField(
        'Артикул',
    )
    start_check = models.DateField(
        verbose_name='Начало периуда'
    )
    end_check = models.DateField(
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
    
    def __str__(self) -> str:
        return f'Трекер товара #{self.article}'


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
        on_delete=models.PROTECT,
        verbose_name='Трекер',
    )

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        ordering = ('-date',)

    def __str__(self) -> str:
        return self.title[:30]
