# -*-  coding = utf-8 -*-
# @Time : 2023/5/7 14:07
# @Autor : 棒棒糖
# @File : util.py
# @Software : PyCharm


from rest_framework.response import Response

def response(data,status=True,size=None,page=None,total=None):
    return Response(
        data={
            "data":data,
            "page":page,
            "size":size,
            "status":status,
            "total":total,
        }
    )