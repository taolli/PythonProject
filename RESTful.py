import requests
def put(self, uri, params=None):
    '''
    封装你自己的put方法，uri是访问路由，params是put请求需要传递的参数，如果没有参数这里为空
    :param uri: 访问路由
    :param params: 传递参数，string类型，默认为None
    :return: 此次访问的response
    '''
    url = self.url_root + uri
    if params is not None:
        # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
        # 返回request的Response结果，类型为requests的Response类型
        res = requests.put(url, data=params)

else:

# 如果无参数，访问方式如下

# 返回request的Response结果，类型为requests的Response类型

res = requests.put(url)

return res


def delete(self, uri, params=None):
    '''
    封装你自己的delete方法，uri是访问路由，params是delete请求需要传递的参数，如果没有参数这里为空
    :param uri: 访问路由
    :param params: 传递参数，string类型，默认为None
    :return: 此次访问的response
    '''
    url = self.url_root + uri
    if params is not None:
        # 如果有参数，那么通过delete方式访问对应的url，并将参数赋值给requests.delete默认参数data
        # 返回request的Response结果，类型为requests的Response类型
        res = requests.delete(url, data=params)
    else:
        # 如果无参数，访问方式如下
        # 返回request的Response结果，类型为requests的Response类型
        res = requests.delete(url)
    return res