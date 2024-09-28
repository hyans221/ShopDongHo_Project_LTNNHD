"""
URL configuration for ShopDongHo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
urlpatterns = [
    # path("admin/", admin.site.urls),
    path('admincustom/', include('admincustom.urls')),
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('product/<MaSP>', product, name='product'),
    path('add_to_cart/<str:MaSP>/', add_to_cart, name='add_to_cart'),
    path('cart/remove_from_cart/<str:MaSP>/', remove_from_cart, name='remove_from_cart'),
    path('dat_hang/', dat_hang, name='dat_hang'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signin/', signin, name='signin'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
