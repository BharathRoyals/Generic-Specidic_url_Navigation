from django.contrib import admin
from django.urls import path
from app1.views import *
 app_name="app1"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bharath/',bharath,name='bharath'),
]