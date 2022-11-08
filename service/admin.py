from django.contrib import admin


from service.models import ServiceDetail
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'image_little_preview', 'text_under_image', 'image_big_preview', 'slug')
    list_display_links = ('id', 'service')
    prepopulated_fields = {'slug': ('service',)}
admin.site.register(ServiceDetail, ServiceDetailAdmin)


from service.models import ServiceDetailArticle
from service.forms import ServiceDetailArticleForm
class ServiceDetailArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'title', 'text', 'is_activated')
    form = ServiceDetailArticleForm
    list_display_links = ('id', 'title')
admin.site.register(ServiceDetailArticle, ServiceDetailArticleAdmin)


from service.models import ServiceListArticle
from service.forms import ServiceListArticleForm
class ServiceListArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'is_activated')
    form = ServiceListArticleForm
    list_display_links = ('id', 'title')
admin.site.register(ServiceListArticle, ServiceListArticleAdmin)

