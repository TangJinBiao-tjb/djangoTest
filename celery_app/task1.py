# -*-  coding = utf-8 -*-
# @Time : 2023/5/14 13:21
# @Autor : 棒棒糖
# @File : task1.py
# @Software : PyCharm

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoTest.settings")
import django
django.setup()
import random
from celery_app import app


# 加入装饰器变成异步的函数
from order.models import User


@app.task
def add():
    i=random.randint(0,10000)
    print(i)
    User.objects.create(name=f"棒棒糖{i}", sex="男")
    print("创建成功")

