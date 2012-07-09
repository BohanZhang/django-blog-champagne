# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    users = models.ForeignKey(User)
    date = models.DateTimeField('发布日期',auto_now_add=True)
    content = models.TextField('内容',null=True,blank=True)
    title = models.CharField('标题',max_length=200,null=True,blank=True)
    status = models.CharField('发布状态',max_length=20,default='publish') 
    name = models.CharField('发布名称',max_length=20,default='open') 
    date = models.DateTimeField('修改日期',auto_now=True)
    parent = models.IntegerField('父类',default=0)
    menu_order = models.CharField('menu_order',max_length=20,default='0') 
    p_type = models.CharField('页面类型',max_length=20,default='post') 
    #comment = models.CharField('评论状态',max_length=20,default='open') 
