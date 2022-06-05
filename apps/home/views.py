# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage , FlexSendMessage
from line_bot.flex_messages import FlexMessages
from line_bot.connecting_line_server import SendFlexMessages
from apps.home.models import *



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return HttpResponseRedirect(reverse('admin:index'))




@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def liffmainpage(request,userId):
    print ('UserId ผู้ใช้งานคือ {}'.format(userId))
    # ทำการ query check ว่า userId นี้ เคยมีการลงทะเบียนมาแล้วหรือไม่
    # หากยังไม่เคยลงทะเบียน ให้ส่งไปที่หน้า ลงทะเบียน
    # หากเคยลงทะเบียนแล้ว ให้ส่งไปที่หน้า liff_index.html
    result = PersonUser.objects.filter(user_userid=userId).first()
    if not result :
        print ('ไม่พบรายชื่อผู้เข้าใช้งาน')
        line_token = LineSetting.objects.all().first()
        line_bot_api = LineBotApi(line_token.line_token)
        user_id = userId
        profile = line_bot_api.get_profile(user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)
        print(profile.status_message)
        # return render(request,'home/line_liff/liff_form.html')
        return render(request,'home/line_liff/liff_form.html',{'display_name':profile.display_name,'user_id':profile.user_id})
    else :
        print ('รายชื่อ userId ที่เข้าใช้งานคือ {}'.format(result.user_userid))
        return render(request,'home/line_liff/liff_index.html')
