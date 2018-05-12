# 引入哈希库
import hashlib
# 引入message(依赖django默认的中间件)
from django.contrib import messages
# 引入重定向函数
from django.shortcuts import redirect
# 引入反向解析函数
from django.core.urlresolvers import reverse


# 对post请求进行封装
def post(request, key):
    return request.POST.get(key, '').strip()


# 对get请求进行封装
def get(request, key):
    return request.GET.get(key, '').strip()


# 设置cookie(24小时)
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获取cookie
def get_cookie(request, key):
    return request.COOKIES.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 删除session(清除所有的session)
def del_session(request):
    request.session.flush()




# 用户密码加密(使用sha256进行加密)
def password_encryption(password, salt='zhaozhao'):

    sha = hashlib.sha256()
    new_password = password + salt
    sha.update(new_password.encode('utf-8'))

    return sha.hexdigest()



# 为message添加单条消息
def add_message(request, key, value):
    messages.add_message(request, messages.INFO, key + ":" + value)


# 获取所有message信息
def get_messages(request):
    # 取出所有错误信息
    all_mess = messages.get_messages(request)
    # 保存错误信息到字典中
    mess_dic = dict()
    for mess in all_mess:
        content = str(mess).split(':')
        mess_dic[content[0]] = mess_dic[1]

    return mess_dic
