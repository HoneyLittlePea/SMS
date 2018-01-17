
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from cmdb import views          #从cmd中导入views.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="L"),     #定义url login的别名为L
    #访问login.html时，执行函数login
    path('userinfo.html',views.userinfo),
    path('home.html',views.Homepage.as_view()),
    #访问home.html时，执行views中的类型Homepage的as_view()方法 【固定用法】

    path('server',views.Server.as_view()),      #访问url server时，执行views.py中的类Server中的方法
    # path('detail',views.Detail.as_view()),      #同理
    # path(r'detail-(\d+)',views.Detail.as_view()),      #同理
    re_path('detail-(?P<nid>\d+)',views.Detail.as_view()),      #正则匹配"detail-数字"
]