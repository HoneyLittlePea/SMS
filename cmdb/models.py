from django.db import models

# Create your models here.

class Userinfo(models.Model):
    #Django会自动创建一个id列，自增，主键

    #定义列username，类型为char,长度为32
    username = models.CharField(max_length=32)

    # 定义列password，类型为char,长度为64
    password = models.CharField(max_length=64)
