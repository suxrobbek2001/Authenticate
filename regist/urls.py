
from django.contrib import admin

from django.urls import path

from app1.views import home,Login,registr,Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('', Login,name='login'),
    path('registr/', registr,name='registr'),
    path('logout/', Logout, name='logout'),
]
