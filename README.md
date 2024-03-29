# EasierDjango
打造更好用的Django

> Django是python实现的重量级的web框架,特点是,写的少,做的多,架构合理,容易维护,django为我们提供了大量的实用功能,但函数的名字不太好记,为了让django更好用,我们可以按照自己的使用习惯,对Django基础功能函数进行二次封装,打造更好用的django


> ![Django_wrappers](http://upload-images.jianshu.io/upload_images/3203841-8d775fe81cc71ae5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 对`get`请求`post`请求 进行封装

```python
# 对post请求进行封装
def post(request, key):
    return request.POST.get(key, '').strip()


# 对get请求进行封装
def get(request, key):
    return request.GET.get(key, '').strip()
```

## 对`cookie`方法进行封装


```python
# 设置cookie(24小时)
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获取cookie
def get_cookie(request, key):
    return request.COOKIES.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)
```

## 对`session`进行封装

```python
# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 删除session(清除所有的session)
def del_session(request):
    request.session.flush()
```


##对`sha256`加密算法进行封装

```python

# 引入哈希库
import hashlib

# 用户密码加密(使用sha256进行加密)
def password_encryption(password, salt='zhaozhao'):

    sha = hashlib.sha256()
    new_password = password + salt
    sha.update(new_password.encode('utf-8'))

    return sha.hexdigest()
```


## 对中间件message方法进行封装



```python
# 引入message(依赖django默认的中间件)
from django.contrib import messages

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
```
>文章涉及到的资源我会通过百度网盘分享，为便于管理,资源整合到一张独立的帖子，链接如下:
http://www.jianshu.com/p/4f28e1ae08b1