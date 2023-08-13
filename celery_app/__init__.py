# -*-  coding = utf-8 -*-
# @Time : 2023/5/14 13:19
# @Autor : 棒棒糖
# @File : __init__.py.py
# @Software : PyCharm


from celery import Celery

app = Celery('celery_app')

app.config_from_object('celery_app.celeryconfig')
