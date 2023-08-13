# -*-  coding = utf-8 -*-
# @Time : 2023/5/14 13:22
# @Autor : 棒棒糖
# @File : task2.py
# @Software : PyCharm


from celery_app import app

@app.task
def multiply(x, y):
    print("JJJJJJJJJJJJJJJJJJJJJ")
    print(x * y)