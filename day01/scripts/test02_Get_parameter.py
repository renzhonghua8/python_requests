"""
    目标：get 请求方法带参演练
    案例：
    1.http:www.baidu.com?id=1001
    1.http:www.baidu.com?id=1001,1002
    1.http:www.baidu.com?id=1001&kw=北京

    请求：
        1.请求方法 get
    参数：
        params:字典或者字符串（推荐字典）
    响应：
        2.响应对象.url #获取请求url
        3.响应对象.status_code #获取响应状态码
        4.响应对象.text #以文本形式显示响应内容

"""
# 1.导包
import requests
# 2.调用get
url = "http://www.baidu.com"
# 案例1 定义字典
# params = {"id":1001}
# 请求时带参 params
# 案例1 字符串形式编写
# r = requests.get(url,params="id=1001") #不推荐
# 案例2
# params = {"id":[1001,1002]} #不推荐
# params = {"id":"1001,1002"} # %2c ASCII值为逗号
# 案例 3
params = {"id":"1001","kw":"北京"} # 多个键值使用方式
r = requests.get(url, params) # r为响应数据对象
# 3.获取请求url地址
print("请求url",r.url)
# 4.获取响应状态码
print("状态码：",r.status_code)
# 5.获取响应信息 文本形式
print("文本形式内容",r.text)