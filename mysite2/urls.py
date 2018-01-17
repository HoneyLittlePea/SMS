"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
urlpatterns = [
    #所有访问/cmdb的，都会到cmdb下的urls.py中去找url的对应关系
    path('cmdb/',include('cmdb.urls')),

    #所有访问/monitor的，都会都monitor中的urls.py中去找对应关系
    path('monitor/',include('monitor.urls')),
        #注意，后面的“/”不能少
]

# from django.conf.urls import url,include
# urlpatterns = [
#     url('^cmdb/',include('cmdb.urls')),
#     url('^monitor/',include('monitor.urls')),
# ]





# from django.urls import re_path
#
# from cmdb import views          #从cmd中导入views.py
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/', views.login, name="L"),     #定义url login的别名为L
#     #访问login.html时，执行函数login
#     path('userinfo.html',views.userinfo),
#     path('home.html',views.Homepage.as_view()),
#     #访问home.html时，执行views中的类型Homepage的as_view()方法 【固定用法】
#
#     path('server',views.Server.as_view()),      #访问url server时，执行views.py中的类Server中的方法
#     # path('detail',views.Detail.as_view()),      #同理
#     # path(r'detail-(\d+)',views.Detail.as_view()),      #同理
#     re_path('detail-(?P<nid>\d+)',views.Detail.as_view()),      #正则匹配"detail-数字"
# ]



