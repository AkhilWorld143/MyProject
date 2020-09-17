"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views
# import these 2 library to work with images for uploading into DB
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Homepage'),
    path('register/', views.register, name='Registraton'),
    path('login/', views.login, name='Login'),
    path('showstudents/', views.showstudents, name='Showstudent'),
    path('update/<int:id>', views.update, name='Update Records'),
    path('delete/<int:id>', views.delete, name='Delete Record'),
    path('change_pass/', views.change_pass, name="Password Change"),
    path('logout/', views.logout),
]
# Add this pattern/path (for URL and for root) to work with images
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
