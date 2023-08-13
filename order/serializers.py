# -*-  coding = utf-8 -*-
# @Time : 2023/5/14 14:14
# @Autor : 棒棒糖
# @File : serializers.py
# @Software : PyCharm
from rest_framework import serializers

from order.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name","sex"]