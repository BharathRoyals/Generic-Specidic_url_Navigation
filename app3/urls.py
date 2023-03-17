from django.contrib import admin
from django.urls import path
from app3.views import *
app_name="app3"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamanth/',hemanth,name='hemanth'),
]