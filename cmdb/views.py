from django.shortcuts import render

# Create your views here.

# from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect       #若想实现跳转，需导入redirect

def login(request):
    # #request包含用户提交的所有信息
    #
    # request.method       #获取用户请求的方法；get、post等
    # request.POST        #封装了POST提交的所有信息，并且是以字典的形式封装的；
    # request.POST.get('user',None)       #获取POST提交过来的K=user的值
    #     #get形式获取key = user的的值，这样即使获取不到，程序不会报错，会返回NONE
    #     #前提是html中input标签有属性name=user,即是定义提交到后台的key

    error_msg = ""                  #error_msg初始值为空
    if request.method == "POST":            ##如果是POST请求，执行下面的；不是，则到render处理去了
        #获取用户提交过来的用户名和密码
        got_user = request.POST.get('user',None)
        got_pwd = request.POST.get('pwd',None)
        if got_user == 'root' and got_pwd == '123':
            return redirect("http://www.baidu.com")     #redirect实现跳转
        else:
            error_msg = "用户名或密码错误"  #验证错误，将error_msg赋值，对应在html页面中用户即可看到提醒信息

    return render(request,"login.html", {"error_msg":error_msg })     #render自动实现了将login.html文件打开响应给用户
        #render打开html文件的过程中，会根据第三个参数（K:V形式）将html中的{{error_message}}进行替换

#
# def login(request):
#     f = open("templates/login.html","r",encoding="utf-8")
#     data = f.read()
#     f.close()
#     return HttpResponse(data)          #将login.html页面响应给用户
#     return render(request,"login.html")