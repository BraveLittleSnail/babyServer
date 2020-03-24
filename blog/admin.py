from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['Article_id','writer','article_title','pub_date','body']
    search_field =['writer']
    list_filter = ['pub_date']

admin.site.register(Article,ArticleAdmin)