"""
    目标：requests库put方法使用
    案例：http://jsonplaceholder.typicode.com/posts/1
    参数：
        1.json：传入json字符串
        2.headers 传入请求信息头内容
    响应：
        1.响应对象.json
"""
# 1.导包
import requests
# 2.调用post
# 定义请求url
url = "http://jsonplaceholder.typicode.com/posts/1"
# 定义请求headers
headers = {"Content-Type":"application/json"}
# 定义请求json
data = {
    "message":[{
            "userId":1,
            "title":"renzhonghua_update",
            "body":"body-body"
               }]

}

r = requests.put(url,json=data,headers=headers)

# 3.获取响应对象
print(r.json())
# 4.获取响应状态码
print(r.status_code)