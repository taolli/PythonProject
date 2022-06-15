'''
# python 代码中引入requests库，引入后才可以在你的代码中使用对应的类以及成员函数
import requests
from common import Common
# 首页的路由
url = '/'
# 实例化自己的Common
comm = Common()
# 调用你自己在Common封装的get方法，返回结果存到了response_index中
response_index = comm.get(url)
# 存储返回的response_index对象text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容:' + response_index.text)
'''

# 登录页路由
from Common import Common

uri = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
comm = Common()
response_login = comm.post(uri, params=payload)
print('Response内容：' + response_login.text)
