# -*- coding: UTF-8 -*-
import json
import sys
import random
import hashlib

import demjson
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.request import RpcRequest
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.authentication import BaseAuthentication
# Response用法 https://www.cnblogs.com/cnhyk/p/12458933.html
from rest_framework.response import Response
from rest_framework.decorators import api_view

from backend import models
from backend.models import myusertwo
from backend.serializers import *

from dateutil import relativedelta
from datetime import datetime
import dateutil, time

SECRET_KEY = 'dhd-rahj2#9h!p6i$o@7^+#vjh3!!x8vyrb-s5iyr=b&_ygimn'


# 生成token
def md5(username):
    m = hashlib.md5(bytes(username, encoding='utf-8'))
    m.update(bytes(SECRET_KEY + str(time.time()), encoding='utf-8'))
    return m.hexdigest()


# 基于token的用户认证
class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 在请求头的query_params中获取token
        # token = request.query_params.get('token')

        # 直接在请求头中获取token
        tokenb = request._request.GET.get('token')
        # 查询是否相等 返回的是Qxx 对象数组（列表）
        token_obj = myusertwo.objects.exclude(token=tokenb)

        if not token_obj:  # token不存在
            raise exceptions.AuthenticationFailed("用户认证失败")
        else:
            datetime_now = datetime.now()

            if token_obj[0].expiration_time > datetime_now:
                # 在rest_framework 内部会将两个字段赋值给 request，以供后续操作
                return token_obj[0].user, token_obj  # 注意将关联的User表对象和token返回出去
            else:
                raise exceptions.AuthenticationFailed("用户toke过期，请重新登陆")


# 用户登陆接口
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            # Django存入数据库的密码是被加过密的 不能直接比较
            password = request.data["password"]
            # print(password)
            user_obj = User.objects.filter(username=username).first()

            if user_obj:
                # 为用户创建token并加密
                token = md5(username)
                # 保存（存在就更新 不存在就创建，并设置过期时间为24小时）
                exceptions_time = datetime.now() + dateutil.relativedelta.relativedelta(minutes=60 * 24)
                defaults = {
                    "token": token,
                    "expiration_time": exceptions_time
                }
                myusertwo.objects.update_or_create(user=user_obj, defaults=defaults)
                return Response(data={'token': token}, status=status.HTTP_200_OK)
            else:
                return Response(data={'error': '用户名或密码错误1'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response(data={'error': '用户名或密码错误2'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 商品接口
class GoodsView(APIView):
    # https://blog.csdn.net/zhubaoJay/article/details/92064067
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.auth)
        try:
            goods_data_list = [
                {'id': 1, 'goods_name': "草莓", 'price': 19.99, 'status': True},
                {'id': 2, 'goods_name': "香蕉", 'price': 9.88, 'status': True},
                {'id': 3, 'goods_name': "苹果", 'price': 5.99, 'status': True},
                {'id': 4, 'goods_name': "蓝莓", 'price': 9.99, 'status': True},
            ]
            return Response({"code": 200, "msg": "商品接口", "data_list": goods_data_list})
        except Exception as e:
            print(e)
            return Response({"code": 500, "error": "接口维护中..."})


# 用户信息接口
class UserInfoView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            # request.user 一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。类型：SimpleLazyObject 值是username
            # 如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。
            username = request.user.username
            # username = request.user
            print(username)
            print(type(username))
            # filter（）的参数可以是字符串，也可以是SimpleLazyObject
            user_obj = User.objects.filter(username=username).first()
            # print("=============")
            # print(user_obj)
            # print(type(user_obj))
            data = {}
            data["username"] = user_obj.username
            data["user_type"] = user_obj.extension.user_type
            data["add_time"] = user_obj.extension.add_time
            return Response({"code": 200, "msg": "查询成功", "userinfo": data})
        except Exception as e:
            print(e)
            return Response({"code": 500, "error": "接口维护中..."})


# 生成6位小写验证码
def generate_verification_code_v2():
    code_list = []
    for i in range(2):
        random_num = random.randint(0, 9)
        a = random.randint(65, 90)
        b = random.randint(97, 122)
        random_lowercase_letter = chr(b)
        code_list.append(str(random_num))
        code_list.append(random_lowercase_letter)
        code_list.append(random_lowercase_letter)
    verification_code = ''.join(code_list)
    return verification_code


# 配置部分（不会变更）
REGION = "cn-hangzhou"
PRODUCT_NAME = "SMSapi"
DOMAIN = "dysmsapi.aliyuncs.com"
ACCESS_KEY_ID = ''  # 必填
ACCESS_KEY_SECRET = ''  # 必填

# 初始化
acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.modify_point(PRODUCT_NAME, REGION, DOMAIN)


class SendSmsRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Dysmsapi', '2017-05-25', 'SendSms')

    def set_TemplateCode(self, TemplateCode):
        """ 模板CODE """
        self.add_query_param('TemplateCode', TemplateCode)

    def set_TemplateParam(self, TemplateParam):
        """ 模板参数，变量 """
        self.add_query_param('TemplateParam', TemplateParam)

    def set_PhoneNumbers(self, PhoneNumbers):
        """ 要发送的手机号 """
        self.add_query_param('PhoneNumbers', PhoneNumbers)

    def set_SignName(self, SignName):
        """ 短信签名名称 """
        self.add_query_param('SignName', SignName)


def send_sms(phone_numbers, sign_name='ABC商城', template_code='SMS_197895983',
             template_param='{"code":"换成自已的"}'):
    """
    调用短信接口，返回结果
    :param phone_numbers:   手机号
    :param sign_name:   短信签名名称
    :param template_code:   模板CODE
    :param template_param:  模板参数，变量
    """
    sign_name = sign_name
    sms_request = SendSmsRequest()
    sms_request.set_TemplateCode(template_code)  # 短信模板CODE
    if template_param:
        sms_request.set_TemplateParam(template_param)  # 短信模板验证码变量
    sms_request.set_SignName(sign_name)  # 短信签名
    sms_request.set_PhoneNumbers(phone_numbers)  # 要发送的手机号
    sms_response = acs_client.do_action_with_exception(sms_request)  # 调用短信发送接口，返回json
    return sms_response


# sss=send_sms('15323441764')
# 返回验证码和是否成功信息给SSS          ,同时往手机发送验证码
def SMS(request, id):  # 参数为手机号,字符串
    myphone = id  # 拿到手机号
    print('获得手机号', myphone)
    message = {}
    # 生成验证码
    smscode = generate_verification_code_v2()
    print(smscode)
    param = str({"code": smscode})

    # 1.发送验证码,2.返回发送状态
    sss = send_sms(myphone, 'ABC商城', 'SMS_197895983', param)

    # 转换类型
    xx = sss
    print("sss", sss)
    t = xx.decode()  # 先变为中文
    jsonbb = t.encode('utf-8')

    print(jsonbb, type(jsonbb))
    # eval函数的作用是将传入的字符串的表达式结果输出来，对象通常是字符串！
    hh = eval(jsonbb)
    print(hh, type(hh))  # 此时hh为字典对象

    MM = hh["Code"]
    CC = hh["Message"]  # 取返回的状态符

    if MM == "OK" and CC == "OK":
        print("信息发送成功")
        message = {"Code": 200, "code": smscode}  # 把状态码和验证码发到前端,校验
    # message= json.dumps(message)#由字典对象转为json对象
    else:
        message = {}  # 把状态码和验证码发到前端,校验
    print("message", message)
    return JsonResponse(message, safe=False, json_dumps_params={'ensure_ascii': False})


# 手机验证码登陆,写入数据库
class mywrite(APIView):
    def post(self, request, *args, **kwargs):
        try:
            UserName = request.data["username"]
            # json.loads(request.body["username"])
            # request.POST.get('username')
            PassWord = request.data["password"]
            # json.loads(request.body["password"])

            # print(request.body)
            # print(json.loads(request.body))
            print("88888", UserName, PassWord)
            newuser = User.objects.create_user(username=UserName, password=PassWord)
            print("newuser", newuser)  # User表中信息已写入了
            print("newuser", type(newuser))

            if newuser:
                # 为登录用户创建token
                token = md5(UserName)
                # 保存(存在就更新不存在就创建，并设置过期时间为24小时)
                expiration_time = datetime.now() + dateutil.relativedelta.relativedelta(minutes=60 * 24)

                defaults = {
                    "token": token,
                    "phone": UserName,
                    "expiration_time": expiration_time
                }
                # newuser 是User类的实例 user=newuser就算在User表中查询与newuser这个对象一致的对象(数据库中的一行)
                myusertwo.objects.update_or_create(user=newuser, defaults=defaults)
                print("后端给前端发送token和用户信息成功")
                return JsonResponse({"code": 200, "token": token, "username": UserName,
                                     "people_img": "./../../../static/myimg/ddd3-03.png"}, safe=False)
            else:
                print("后端给前端发送token和用户信息失败")
                return HttpResponse({""})
        except Exception as e:
            print(e)
            print("代码逻辑错误")
            return HttpResponse({"系统出错"})


def mywrite2(request):
    try:
        UserName = request.POST.get('username')
        # json.loads(request.body["username"])
        # request.POST.get('username')
        PassWord = request.POST.get('password')
        # json.loads(request.body["password"])

        print(request.body)
        # print(json.loads(request.body))
        print("88888", UserName, PassWord)
        newuser = User.objects.create_user(username=UserName, password=PassWord, email="xxx@qq.com")
        print("newuser", newuser)  # User表中信息已写入了

        if newuser:
            # 为登录用户创建token
            token = md5(UserName)
            # 保存(存在就更新不存在就创建，并设置过期时间为24小时)
            expiration_time = datetime.now() + dateutil.relativedelta.relativedelta(minutes=60 * 24)

            defaults = {
                "token": token,
                "phone": UserName,
                "expiration_time": expiration_time
            }
            myusertwo.objects.update_or_create(user=newuser, defaults=defaults)
            print("后端给前端发送token和用户信息成功")
            return JsonResponse({"code": 200, "token": token, "username": UserName, "people_img": "./../../../static"
                                                                                                  "/myimg/ddd3-03.png"},
                                safe=False)
        else:
            print("后端给前端发送token和用户信息失败")
            return HttpResponse({""})
    except Exception as e:
        print(e)
        print("代码逻辑错误")
        return HttpResponse({"系统出错"})


# 查询所以产品
@api_view(['GET', 'POST'])
def get_proudct(request, format=None):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # elif request.method == 'POST':
    #     serializer = ProductSer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 用于读写 - 删除端点以表示单个模型实例。
# 提供get，put，patch和delete方法处理。
# 下面两个都是父类中已有的的变量
# 外键user接收参数为user而不是user_id
class Address(RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSer


# ListAPIView用于只读端点以表示模型实例的集合。
# 提供get方法处理程序
class AllAddress(ListAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSer

# POST的uer_id字段用user代替，貌似rest_framework子类CreateAPIView
# 会自动处理成user_id然后添加。直接用user_id是找不到对应字段的
class CreatAddress(CreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = CreatUserAddressSer


@api_view(['GET', 'POST'])
def get_address(request, id, format=None):
    user_data = User.objects.filter(username=id).first()
    address_data = user_data.uextension.all()
    # print(address_data)
    serializer = UserAddressSer(address_data, many=True)
    return Response(serializer.data)


# 生成订单编号serial number
def generate_order_code():
    order_sn = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', ''))[-7:]
    return order_sn


@api_view(['GET', 'POST'])
def order_add(request):
    try:
        # # request.body 是原生数据类型
        # # 传输的数据为编码后的json 格式需要先解码，在转化后才能当作字典来使用
        # body_utf8 = request.body.decode('utf-8')
        # print(type(body_utf8))
        # print(body_utf8)
        # # demjson.encode将 Python 对象编码成 JSON 字符串
        # # demjson.decode将已编码的 JSON 字符串解码为 Python 对象
        # # 直接用json.loads有缺陷
        # body_str_json = demjson.encode(body_utf8)
        # print(type(body_str_json))
        # print(body_str_json)
        # # 与数据为json字符串，loads一次将json转化为字典字符串，两次转化为字典对象
        # body_str_dic = json.loads(body_str_json)
        # body_dic = json.loads(body_str_dic)
        # print(type(body_dic))
        # print(body_dic)
        # Username = body_dic['username']
        # AddressId = body_dic['addressid']
        # ProductId = body_dic['productid']
        # ProductNum = body_dic['pnum']
        # MyPrice = body_dic['myprice']

        # 由于前端POST传回数据 默认一般为application/x-www-form-urlencoded
        # "username=TIANYUZHOU&addressid=1&productid=3&myprice=89&pnum=3"
        # 直接用封装好的POST方法简单
        if request.method == 'POST':
            Username = request.POST.get('username')
            AddressId = request.POST.get('addressid')
            ProductId = request.POST.get('productid')
            ProductNum = request.POST.get('pnum')
            MyPrice = request.POST.get('myprice')

            order_sn = generate_order_code()
            print(order_sn)

            user = User.objects.filter(username=Username).first()
            user_id = user.id
            print(type(user))
            print("用户id", user_id)
            # product = Product.objects.filter(id=ProductId).first()
            # address = UserAddress.objects.filter(id=AddressId).first()
            # 对与外键可以使用模型类的实例，而可以不是具体的参数值。
            # 例如 User 传user=user也可以user_id =user_id
            # order_obj = models.OrderInfo.objects.create(user=user, product=product, address=address,
            #                                           product_num=ProductNum, order_sn=order_sn,
            #                                           post_script="发正品", order_amount=MyPrice)
            order_obj = models.OrderInfo.objects.create(user_id=user_id, product_id=ProductId, address_id=AddressId,
                                                        product_num=ProductNum, order_sn=order_sn,
                                                        post_script="发正品", order_amount=MyPrice)

            serializer = OrderInfoSer(order_obj)
            print("订单已写入")

            if order_obj:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                print("写入订单失败")
                return HttpResponse("订单写入失败！")
    except Exception as e:
        print(e)
        return HttpResponse("发生错误！")


# 查询所有分类
@api_view(['GET', 'POST'])
def get_category(request, format=None):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySer(category, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = CategorySer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 查询指定类别下的产品
@api_view(['GET', 'POST'])
def assign_category_pd(request, id, format=None):
    if request.method == 'GET':
        category = Category.objects.filter(id=id)[0]
        print(type(id))
        # print(category)
        # 通过外键获得该表对应下的子表
        product = category.product_set.all()
        serializer = ProductSer(product, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = CategorySer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
