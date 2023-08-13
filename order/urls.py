# -*-  coding = utf-8 -*-
# @Time : 2023/5/7 12:50
# @Autor : 棒棒糖
# @File : urls.py
# @Software : PyCharm


from django.urls import path

from order.views.test import Test

urlpatterns = [
    path('test', Test.as_view()),
]