from django.db import models

from django.utils import timezone
# Create your models here.


class User(models.Model):
    '''用户表'''

    gender = (
        ('男', '男'),
        ('女', '女'),
    )


    name = models.CharField(max_length=128, unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    url = models.URLField()
    u_time = models.DateTimeField()
    c_time = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.u_time = timezone.now()
        super(User, self).save(*args, **kwargs)
