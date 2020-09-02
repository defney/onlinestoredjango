"""dprojx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# dprojx/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url #,include
from dappx import views
from django.conf.urls.static import static
from dprojx import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^dappx/',include('dappx.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^details',views.details,name='details'),
    path('<int:product_id>/',views.details,name='details'),
    url(r'^salesmanager',views.salesmanager,name='salesmanager'),
    url(r'^productmanager',views.productmanager,name='productmanager'),
  	#path(r'^cart/<int:pr_id>/', views.cart, name='cart'),
    #path(r'^cart/', views.cart, name='cart'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^account$', views.account, name='account'),
    url(r'^cart', views.cart, name='cart'),
    path('<int:pr_id>/', views.cart, name='cart'),
    url(r'^remove_item', views.remove_item, name='remove_item'),
    path('<int:pr_id>/', views.remove_item, name='remove_item'),
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^checkout_complete/$',views.checkout_complete,name='checkout_complete'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
