from django.contrib import admin
from open_image.models import NewsWebsite, Article, Den

class NewsWebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)

    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'news_website', 'url_',)
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True

class DenAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')

admin.site.register(NewsWebsite, NewsWebsiteAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Den, DenAdmin)