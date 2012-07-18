# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from blog.models import Posts
from django.http import HttpResponse
from comment.models import Comment 
import uuid
@csrf_exempt
def post(request):
    """
    提交评论
    """
    # 返回信息
    msg = '评论成功！'

    # 验证GET或POST
    if request.method == 'GET':
        msg = '不要乱玩哦亲：提交方式为GET'
        return HttpResponse(msg, 'application/javascript')
    post = request.POST

    # 取得文章
    post_id = post.get('post_id', None)
    if not post_id:
        msg = '不要乱玩哦亲：post_id为空'
        return HttpResponse(msg, 'application/javascript')
    posts = Posts.objects.get(id=post_id)

    # 处理账号信息
    author = post.get('author', '屁民')
    email = post.get('email', '')
    url = post.get('url', '')

    user = User()
    try:
        user = User.objects.get(first_name=author, email=email)
    except User.DoesNotExist:
        # 生成一个不重复和username
        username = uuid.uuid1()
        user.username = username
        user.first_name = author
        user.email = email
        user.last_name = url
        user.save()

    # 处理评论
    contact = post.get('comment', None)
    if not contact or contact.strip() == '':
        msg = '评论不能为空哦！'
        return HttpResponse(msg, 'application/javascript')
    
    comment = Comment()
    comment.contact = contact
    comment.user = user
    comment.post = posts
    comment.save()

    # 返回信息
    return HttpResponse('SUCCESS', 'application/javascript')
