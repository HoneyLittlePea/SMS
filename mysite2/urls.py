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

# urlpatterns = [
#     url(r'^pattern ', func)     ##无论是否正则，都这样写
# ]
#
# #Django 2.0.1
# from django.urls import path
# from django.urls import re_path
# urlpatterns = [
#     path(' ',func)                  #无正则时
#     re_path(' pattern ',func)       #有正则时
# ]


# url正定义正则时，可以直接定义Django来调用时的参数名称
#比如，此处定义第一个匹配的结果参数名称为gid,第二个结果名称为uid
# re_path('detail-(?P<gid>\d+)-(?P<uid>\d+)', views.Detail.as_view()),
# #
# # #比如匹配结果为：http://127.0.0.1:8000/detail-1-9
# def Detail(request,uid,gid):    #此处传递参数时，必须使用名称gid和uid，但此时顺序无所谓了
#     request.GET.get("uid")          #结果是9
#     request.GET.get("gid")          #结果是1