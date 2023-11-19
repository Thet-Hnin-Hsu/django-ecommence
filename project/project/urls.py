"""project URL Configuration

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
    2. Add a URL to urlpatterns:  path('app/', include('app.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.to_home),

    path('admin/', admin.site.urls),

    path('app/list/', views.list),

    path('app/detail/<int:product_id>/', views.detail),

    path('app/orderpage/<int:product_id>/', views.orderpage),

    path('app/order/<int:product_id>/', views.order),

    path('app/order/list/<int:user_id>/', views.order_list),

    path('app/order/detail/<int:order_id>/', views.order_detail),

    path('login/', views.login_view, name="login"),

    path('register/', views.register_view, name="register"),

    path('logout/', views.logout_view),

    path('app/cmt/create/<int:product_id>/', views.cmt_create),

    path('app/cmt/delete/<int:product_id>/<int:cmt_id>/', views.cmt_delete),

    path('app/cmt/update/<int:product_id>/<int:cmt_id>/', views.cmt_update),

    path('app/search_by/', views.search_by),
    re_path(r'^.*/$', views.custom_404_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
