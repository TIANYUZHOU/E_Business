from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import views

from backend.views import *



urlpatterns = [

    path('get_pd/',get_proudct),
    path('get_cg/',get_category),
    path('ueditor/',include('DjangoUeditor.urls')),
    path('assign_cg_pd/<id>/',assign_category_pd),
    path('login/',LoginView.as_view()),
    path('goods/',GoodsView.as_view()),
    path('userinfo/',UserInfoView.as_view()),
    path('SMS/<id>/',SMS,name='SMS'),
    path('mywrite/<idx>/<idy>/',mywrite.as_view()),
    # 登陆信息写入数据库（验证码）
    path('mywrite/',mywrite2),
    # 在rest_framework子类中应该 定义的形参就是pk对应数据库中id字段
    # 不能自定义,除非在函数内部再传一次参数给pk或直接使用自定义函数
    path('address/<pk>',Address.as_view()),
    path('address_all/',AllAddress.as_view()),
    path('create_address/',CreatAddress.as_view()),
    path('get_address/<id>',get_address),
    path('order_add/',order_add)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)