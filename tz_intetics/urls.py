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
from django.contrib import admin
from django.urls import path, re_path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('admin_login/', views.LoginView.as_view(), name='admin_login'),
    path('list/', views.Show.list, name='list'),
    path('register/', views.Show.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('list/user/<int:user_id>/', views.Show.user, name='user'),
    path('list/user/new_car/<int:user_id>/', views.Show.new_car, name='new_car'),
    path('new_car', views.Show.new_car, name='new_car'),
    re_path(r'(\w+/)*(?P<user_id>[0-9]+)/car/(?P<car_id>[0-9]+)/$', views.Show.car, name='car'),
    path('list/user/<int:user_id>/car/<int:car_id>/car_delete/<int:pk>/', views.CarDelete.as_view(), name='car_delete'),
    # path(' list/user/<int:user_id>/car/<int:car_id>/car_delete/', views.CarDelete.as_view(), name='car_delete'),
    path('list/user/<int:user_id>/car_update/<int:pk>/', views.CarUpdate.as_view(), name='car_update'),
    path('list/user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('list/user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('list/user/<int:user_id>/car/<int:car_id>/new_order/', views.Show.new_order, name='new_order'),
    path('list/user/<int:user_id>/car/<int:car_id>/order_update/<int:pk>/', views.OrderUpdate.as_view(), name='order_update'),
]


