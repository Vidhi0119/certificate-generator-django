from django.contrib import admin
from django.urls import path
from certificates import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  
]
