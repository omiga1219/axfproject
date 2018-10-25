from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
import logging


class Middleware(MiddlewareMixin):

    def process_request(self,request):

        upath = request.path
        auths = request.session.get('auths')
        # print(request.META['REMOTE_ADDR'])

        logger = logging.getLogger('abc')
        logger.info(request.META['REMOTE_ADDR']+'|'+upath)

        #白名单 index
        blist =['/login/','/regist/','/getyzm/','/nameyjy/','/codejy/']



        shopcarlist =['/addshopcar/','/subshopcar/','/selshopcar/']

        name = request.session.get('name')

        # if not name and upath not in shopcarlist:
        #     return render(request,'login.html')
        #
        # if (not upath  in blist)  and (not upath in auths) :
        #     return HttpResponse('你没有对应的权限')