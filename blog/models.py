from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    Article_id = models.IntegerField()
    writer = models.CharField(max_length = 20)
    article_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=2000)
    
    #把从数据库获取的内容返还给前端
    def __str__(self):
        print(self.Article_id)
        return self.body
