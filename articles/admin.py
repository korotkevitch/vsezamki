from django.contrib import admin


from articles.models import ArticleDetail
from articles.forms import ArticleDetailForm
class ArticleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'title', 'slug', 'text', 'created_date', 'image_preview', 'is_activated')
    form = ArticleDetailForm
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(ArticleDetail, ArticleDetailAdmin)


from articles.models import ArticleList
from articles.forms import ArticleListForm
class ArticleListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'is_activated')
    form = ArticleListForm
    list_display_links = ('id', 'title')
admin.site.register(ArticleList, ArticleListAdmin)
