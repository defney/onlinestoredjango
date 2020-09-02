# dappx/urls.py
from django.conf.urls import url
from dappx import views
from django.urls import path
from django.conf.urls.static import static
from dprojx import settings

# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^details/(?P<product_id>\d+)/$',views.details,name='details'),
    url(r'^search/$', views.search, name='search'),
    url(r'^category/(?P<category_name>.*)/$', views.category, name='category'),
    url(r'^listby/(?P<search_filter>.*)/(?P<filter_t>.*)/(?P<minimum_price>.*)/(?P<maximum_price>.*)/$', views.listby, name='listby'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^account$', views.account, name='account'),
    url(r'^view_orders$', views.view_orders, name='view_orders'),
  	#path(r'^cart/<int:pr_id>/', views.cart, name='cart'),
    #path(r'^cart/', views.cart, name='cart'),
    url(r'^cart/(?P<pr_id>.*)/$', views.cart, name='cart'),
    url(r'^remove_item/(?P<pr_id>.*)/$', views.remove_item, name='remove_item'),
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^checkout_complete/$',views.checkout_complete,name='checkout_complete'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
