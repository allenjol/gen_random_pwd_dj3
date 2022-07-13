import logging
from django.shortcuts import render
from django.http import JsonResponse

from .custom_src import src
# from .custom_src import src_v1
# from .custom_src import src_v2

# Create your views here.
logger = logging.getLogger('access_log')

# def index(request):
#     logger.info('访问了index首页!')

#     return HttpResponse('欢迎使用随机密码生成器工具!')


def index(request):
    logger.info('访问了密码生成器首页!')

    return render(request, 'gen_pwd/index.html')


def get_simple_pwd(request):
    pwd_string = src.gen_simple_interface()
    pwd_data = {'password': pwd_string}
    logger.info(f'本次生成的密码为: {pwd_string}')

    return JsonResponse(pwd_data)


def get_complex_pwd(request):
    pwd_string = src.gen_complex_interface()
    pwd_data = {'password': pwd_string}
    logger.info(f'本次生成的密码为: {pwd_string}')

    return JsonResponse(pwd_data)
