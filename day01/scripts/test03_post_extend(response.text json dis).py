"""
    目标：requests库post方法使用
        相应对象.text与响应对象.json() 区别
    案例：http://jsonplaceholder.typicode.com/posts
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
url = "http://jsonplaceholder.typicode.com/posts"
# 定义请求headers
headers = {"Content-Type":"application/json"}
# 定义请求json
data = {
    "message":[{
        "userId":1,
        "title":"renzhonghua",
        "body":"body-body"
            }]

}

r = requests.post(url,json=data,headers=headers)

# 3-1.获取响应对象 json格式
r_json = r.json()
print("r_json:",r_json)
print("r_json类型为:",type(r_json))
print("r_json通过键名获取值:",r_json['message'])
# 3-2.获取响应对象 text格式
r_text = r.text
print("r_text:",r_text)
print("r_text类型为:",type(r_text))
# 预期结果报错，str没有键名一说
print("r_text通过键名获取值:",r_text['message'])
# 4.获取响应状态码
print(r.status_code)