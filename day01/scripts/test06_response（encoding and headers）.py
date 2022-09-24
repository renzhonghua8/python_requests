"""
    目标：响应对象常用方法
    1.encoding
        1.获取请求编码
        2.设置响应编码
    2.headers
        1.获取响应信息头信息
    案例：http://www.baidu.com
"""

# 1.导包
import requests
# 2.调用get方法
url = "http://www.baidu.com"
r = requests.get(url)
# 3.查看默认请求编码ISO-8859-1
print(r.encoding)
# 3-1 设置响应编码
r.encoding = "utf-8"
# 4.查看响应内容，text格式
print(r.text)
# 5.查看响应信息头 提示：headers信息比较重要（项目工作中一般服务器返回的token\session相关信息都在headers中）
print(r.headers)