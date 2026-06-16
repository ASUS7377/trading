from django.contrib import admin
from .models import Profile, Trade
from .models import TodoTask


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'initial_balance',
    )


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'symbol',
        'trade_type',
        'profit',
    )

    list_filter = (
        'trade_type',
        'date',
    )

    search_fields = (
        'symbol',
    )

admin.site.register(
    TodoTask
)