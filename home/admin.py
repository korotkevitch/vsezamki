from django.contrib import admin


from home.models import Head
class HeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview')
    list_display_links = ('id', 'title')
admin.site.register(Head, HeadAdmin)


from home.models import About
from home.forms import AboutForm
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    form = AboutForm
    list_display_links = ('id', 'title')
admin.site.register(About, AboutAdmin)


from home.models import Principle
class PrincipleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image_preview')
    list_display_links = ('id', 'title')
admin.site.register(Principle, PrincipleAdmin)


from home.models import VideoBlock
class VideoBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'intro', 'image_preview', 'link', 'subtitle_1', 'text_1', 'subtitle_2', 'text_2',
                    'subtitle_3', 'text_3', 'label')
    list_display_links = ('id', 'title')
admin.site.register(VideoBlock, VideoBlockAdmin)


from home.models import HomeArticleWithPhoto
from home.forms import HomeArticleWithPhotoForm
class HomeArticleWithPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image_preview')
    form = HomeArticleWithPhotoForm
    list_display_links = ('id', 'title')
admin.site.register(HomeArticleWithPhoto, HomeArticleWithPhotoAdmin)


from home.models import HomeArticle
from home.forms import HomeArticleForm
class HomeArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'is_activated')
    form = HomeArticleForm
    list_display_links = ('id', 'title')
admin.site.register(HomeArticle, HomeArticleAdmin)

