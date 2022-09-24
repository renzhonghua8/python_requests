"""
    目标：requests库post方法使用 参数(data与json区别)
    案例：http://jsonplaceholder.typicode.com/posts
    将字典对象转换为json字符串：
        1.导入json
        2.dumps(dict)
    参数：
        1.json：传入json字符串
        2.headers 传入请求信息头内容
    响应：
        1.响应对象.json
"""
# 1.导包
import json

import requests
# 2.调用post
# 定义请求url
url = "http://jsonplaceholder.typicode.com/posts"
# 定义请求headers
headers = {"Content-Type":"application/json"}
# 定义请求json
data = {
    "userId":1,
    "title":"renzhonghua",
    "body":"body-body"
}
# 使用json方式新增——>成功
# r = requests.post(url,json=data,headers=headers)
# 使用data方式新增——>失败
# 注意：对于python字典和json虽然长得一样，但是数据序列格式还是有一定的区别
# r = requests.post(url,data=data,headers=headers)
# 将字典对象转为json字符串
r = requests.post(url,data=json.dumps(data),headers=headers)
# 3.获取响应对象
print(r.json())
# 4.获取响应状态码
print(r.status_code)