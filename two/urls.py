from django.conf.urls import url
from django.contrib import admin

from two import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^addBuyer/", views.addBuyer),
    url(r"^addGoods/", views.addGoods),
    url(r"^addGoodsAndBuyer/", views.addGoodsAndBuyer),
    url(r"^delBuyer/", views.delBuyer),
    url(r"^delGoods/", views.delGoods),
]