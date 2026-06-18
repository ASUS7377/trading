from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):

    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )

    initial_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Начальный депозит"
    )

    target_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цель"
    )

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )
    is_setup_completed = models.BooleanField(
        default=False
    )
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name


class Trade(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Пользователь'
    )

    ASSETS = (

        ('XAUUSD', 'Gold (XAUUSD)'),
        ('XAGUSD', 'Silver (XAGUSD)'),

        ('BTCUSD', 'Bitcoin (BTCUSD)'),
        ('ETHUSD', 'Ethereum (ETHUSD)'),

        ('EURUSD', 'EUR/USD'),
        ('GBPUSD', 'GBP/USD'),

        ('NAS100', 'NASDAQ 100'),
        ('US30', 'Dow Jones'),

        ('SPX500', 'S&P 500'),
    )

    TRADE_TYPES = (

        ('BUY', 'BUY'),
        ('SELL', 'SELL'),
    )

    TRADE_RESULTS = (

        ('TP', 'Take Profit'),
        ('SL', 'Stop Loss'),
        ('MANUAL', 'Ручное закрытие'),
    )

    date = models.DateField(
        verbose_name='Дата сделки'
    )

    symbol = models.CharField(
        max_length=30,
        choices=ASSETS,
        verbose_name='Актив'
    )

    trade_type = models.CharField(
        max_length=10,
        choices=TRADE_TYPES,
        verbose_name='Тип'
    )

    profit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Прибыль / Убыток'
    )

    lot_size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Лот'
    )

    entry_price = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        default=0,
        verbose_name='Цена входа'
    )

    exit_price = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        default=0,
        verbose_name='Цена выхода'
    )

    take_profit = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        null=True,
        blank=True,
        verbose_name='Take Profit'
    )

    stop_loss = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        null=True,
        blank=True,
        verbose_name='Stop Loss'
    )

    trade_result = models.CharField(
        max_length=20,
        choices=TRADE_RESULTS,
        default='MANUAL',
        verbose_name='Результат сделки'
    )

    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )

    screenshot = models.ImageField(
        upload_to='trades/',
        blank=True,
        null=True,
        verbose_name='Скриншот'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-date', '-id']

        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):

        return (
            f'{self.user} | '
            f'{self.symbol} | '
            f'{self.trade_type} | '
            f'{self.profit}$'
        )


class TodoTask(models.Model):

    CATEGORY_CHOICES = [

        ('TRADING', 'Трейдинг'),

        ('STUDY', 'Обучение'),

        ('SPORT', 'Спорт'),

        ('PERSONAL', 'Личное'),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='TRADING'
    )

    deadline = models.DateField(
        null=True,
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title