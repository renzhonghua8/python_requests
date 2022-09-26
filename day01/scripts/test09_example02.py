"""
http://www.testingedu.com.cn:8000/Home/Index/index.html
相关接口：
        获取验证码：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify
        登录接口：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6491552353883769
        登录数据：      data= {
                                "username": "13800138006",
                                "password": "123456"
                                "verify_code": "iqp7"
                                }
        订单：http://www.testingedu.com.cn:8000/Home/Order/order_list.html
"""
# 1.导包
import requests
# 请求验证码
url_verify_code = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify"
r = requests.get(url_verify_code)
# 获取cookies
r_cookie = r.cookies
print("获取的cookie为：",r_cookie)
# 单独获取cookie值
print("获取的cookie值为:",r_cookie['PHPSESSID'])
# 设置cookies变量
cookies = {"PHPSESSID":r_cookie['PHPSESSID']}
# 2.调用post
url_login = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login"
data = {
        "username": "13800138006",
        "password": "123456",
        "verify_code": "iqp7"
}
r = requests.post(url = url_login , data = data, cookies=cookies)
# 3.验证是否登录成功
print(r.json())
# 4.查询我的订单
url_order = "http://www.testingedu.com.cn:8000/Home/Order/order_list.html"
r = requests.get(url=url_order,cookies=cookies)
print(r.text)