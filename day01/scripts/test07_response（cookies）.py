"""
    目标：响应对象常用方法
    1.cookies
        1.获取响应对cookies信息
    2.content
        1.以字节码形式获取响应信息（图片、视频..多媒体格式）
    案例：cookies:http://www.baidu.com
        content:https://www.baidu.com/img/bd_logo1.png?where=super
"""

# 1.导包
import requests
# 2.调用get方法
# url = "http://www.baidu.com"
url_img = "https://www.baidu.com/img/bd_logo1.png?where=super"
# r = requests.get(url)
r = requests.get(url_img)
# 3.获取响应cookies 返回字典对象
# print("cookies信息为：",r.cookies)
# 通过键名获取响应的cookies值
# print("cookies信息为：",r.cookies['BDORZ'])

# 以text文本形式解析图片----->乱码
print(r.text)

# 以字节码形式解析图片
print(r.content)

# 以图片写入当前目录baidu.png
with open("./baidu.png","wb") as f:
    f.write(r.content)
