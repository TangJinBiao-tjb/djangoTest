# -*-  coding = utf-8 -*-
# @Time : 2023/5/14 13:19
# @Autor : 棒棒糖
# @File : celeryconfig.py
# @Software : PyCharm


from datetime import timedelta
from celery.schedules import crontab


BROKER_URL = 'redis://:123456@192.168.2.158:6379/0'
CELERY_RESULT_BACKEND = 'redis://:123456@192.168.2.158:6379/1'
CELERY_TIMEZONE = "Asia/shanghai"
CELERY_RESULT_SERIALIZER = 'msgpack'

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 设置定时任务
CELERYBEAT_SCHEDULE = {
    'task1':{
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=22, minute=20),
        'args': (4, 5)
    }
}


# 启动：
# 终端1：celery -A celery_app beat
# 终端2：celery -A celery_app worker -l info -P eventlet --pool=solo