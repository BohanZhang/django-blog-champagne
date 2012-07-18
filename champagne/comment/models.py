# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from blog.models import Posts

class Comment(models.Model):
    contact = models.TextField('内容')
    create_time = models.DateTimeField('评论时间', auto_now=True)
    mark_delete = models.BooleanField('标记删除', default=False)
    # Foreignkey
    user = models.ForeignKey(User)
    post = models.ForeignKey(Posts)
