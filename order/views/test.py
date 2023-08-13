# -*-  coding = utf-8 -*-
# @Time : 2023/5/7 12:51
# @Autor : 棒棒糖
# @File : test.py
# @Software : PyCharm


from rest_framework.views import APIView

from djangoTest.util import response
from order.models import User
from order.serializers import UserSerializer


class Test(APIView):


    def get(self,request):
        print("get请求")
        return response("成功")

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return response("成功")