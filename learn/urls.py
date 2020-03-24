from django.urls import path
from django.conf.urls import url

from . import views
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url('calculate',views.calculate),
    #url('add',views.add),
    url('getimagelist',views.getimagelist),
]