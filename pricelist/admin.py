from django.contrib import admin


from pricelist.models import Price
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6', 'item_7')
    list_display_links = ('id', 'service')
admin.site.register(Price, PriceAdmin)

