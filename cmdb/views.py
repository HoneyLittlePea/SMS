from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
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

def userinfo(client):
    if client.method == "POST":
        user = client.POST.get("user")
        print("Username is: ",user)

        pwd = client.POST.get("pwd")
        print("Password is: ",pwd)

        gender = client.POST.get("gender")
        print("Gender is :", gender)

        courses = client.POST.getlist("Course")
        print("Courses are: ",courses)

        city = client.POST.get("city")
        print("City is: ", city)

        hobbies = client.POST.getlist("hobbies")
        print("Hobbies are: ", hobbies)

        # filename = client.POST.get("upload")
        # print("Filename is: ",filename)

        # client.FILES
        obj =  client.FILES.get("upload")          ##获取用户上传的文件
        obj.name        #文件名
            #此时print(obj)结果也是文件名，是因为类obj里面定义__str__方法（return self.name）
            #type(obj) 结果： <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>

        import os
        file_name = os.path.join("img",obj.name)    #设置用户上传的目录为img目录
        f = open(file_name,"wb")
        for i in obj.chunks():          #用户上传的文件会按chunk一块块存取
            f.write(i)
        f.close()

    return render(client,"clientform.html")

def test(request):
    request.POST.get("name")           ##获取表单中单个值的方法；如：text,password,radio,select等
    request.POST.getlist("name")       ##获取多个值的方法；如：checkbox, select(multiple)

from django.views import View       ##导入View
class Homepage(View):                               ##必须继承函数View
    def get(self,request):                          ##定义处理get请求的get方法
        return render(request,'home.html')

    def post(self,request):                         ##定义处理post请求的post方法
        return render(request,'home.html')

    #此处可以定义的方法有：
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    #上述能够完成自动判读处理get或post，是因为：
    #在父类View中（由父类中的dispatch()方法实现）会通过反射，读取用户请求头中的RequestMethod，
    # 自动完成判断，GET请求交由get()方法处理，POST请求交由post()方法处理
    #即，请求到来后，会先被父类Veiws中的dispatch()处理，然后再交由get()或post()等处理；
    #所以，继而，在我们自己自定义的类中可以对父类中的dispatch()进行重构，
    # 来实现响应用户之前（即执行get()前），自定义一些功能（具体讲解，见D19V5 00:10:00）

SERVER_LIST = {         ##此处，手动定义数据来源；字典中嵌套一个字典
    "1":{"name":"host001","ip":"192.168.1.1","sshport":"22","location":"SZ"},
    "2":{"name":"host002","ip":"192.168.1.2","sshport":"22","location":"SZ"},
    "3":{"name":"host003","ip":"192.168.1.3","sshport":"22","location":"BJ"},
    "4":{"name":"host004","ip":"192.168.1.4","sshport":"22","location":"BJ"}
}
class Server(View):     #定义类Server，结果会返回模板文件server.html给用户
    def get(self,request):
        return render(request,"server.html",{"SERVER_LIST":SERVER_LIST})
        #会替换模板文件中的变量SERVER_LIST；模板文件中的SERVET_LIST的值为此处的SERVER_LIST;

class Detail2(View):     #定义类Detail，返回模板文件detail.html给用户
    def get(self,request):
        id = request.GET.get("id")          #获取用户get请求时参数id的值（访问地址?id=1中有字段id[GET方法是从地址栏获取]）
        server_detail = SERVER_LIST[id]     #此id值即为列表对应的key，所以由key取V，V也是一个dict
        return render(request,"detail.html",{"server_detail":server_detail})

class Detail(View):
    def get(self,request,nid):       #此时增加一个参数id（名称自定义），
                                    # Django会自动提取url中正则匹配的那个数字，传递给此处的参数id
        server_detail = SERVER_LIST[nid]         #所以此时id可以直接拿来使用，也不用去get了
        return render(request,"detail.html",{"server_detail":server_detail})

def func(request,*args,**kwargs):
    #*agrs接收url中为给名称的，直接传递的参数
    #**kwargs接收url中已定义好名称的参数
    pass
