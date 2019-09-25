"""tz_intetics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from webapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.Show.home, name='home'),
    re_path(r'admin_login/', views.LoginView.as_view(), name='admin_login'),
    re_path(r'list/$', views.Show.list, name='list'),
    re_path(r'register/', views.Show.register, name='register'),
    re_path(r'logout', views.logout, name='logout'),
    re_path(r'(\w+/)*new_car/(?P<user_id>[0-9]+)/$', views.Show.new_car, name='new_car'),
    re_path(r'(\w+/)*user/(?P<user_id>[0-9]+)/$', views.Show.user, name='user'),
    re_path(r'(\w+/)*(?P<user_id>[0-9]+)/car/(?P<car_id>[0-9]+)/$', views.Show.car, name='car'),
    re_path(r'(\w+/)*(?P<user_id>[0-9]+)/car/(?P<car_id>[0-9]+)/car_delete/(?P<pk>[0-9]+)/$', views.CarDelete.as_view(), name='car_delete'),
    re_path(r'(\w+/)*(?P<user_id>[0-9]+)/car_update/(?P<pk>[0-9]+)/$', views.CarUpdate.as_view(), name='car_update'),
    re_path(r'(\w+/)*user_update/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='user_update'),
    re_path(r'(\w+/)*user_delete/(?P<pk>[0-9]+)/$', views.UserDelete.as_view(), name='user_delete'),
    re_path(r'(\w+/)*(?P<user_id>[0-9]+)/car/(?P<car_id>[0-9]+)/new_order/$', views.Show.new_order, name='new_order'),
    re_path(r'(\w+/)*(?P<user_id>[0-9]+)/car/(?P<car_id>[0-9]+)/(\w+/)*order_update/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view(), name='order_update'),
    re_path(r'(\w+/)*user/(?P<user_id>[0-9]+)/car/(?P<car_id>[0-9]+)/(\w+/)*order_delete/(?P<pk>[0-9]+)/$', views.OrderDelete.as_view(), name='order_delete'),
]



