from django.contrib import admin
from django.urls import path
from app2.views import *
app_name="app2"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dhanu/',dhanu,name='dhanu'),
]