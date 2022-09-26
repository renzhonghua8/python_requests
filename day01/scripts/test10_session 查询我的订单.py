"""
http://www.testingedu.com.cn:8000/Home/Index/index.html
相关接口：
        获取验证码：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify
        登录接口：http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6491552353883769
        登录数据：      data= {
                                "username": "13800138006",
                                "password": "123456",
                                "verify_code": "iqp7"
                                }
        订单：http://www.testingedu.com.cn:8000/Home/Order/order_list.html
"""
# 1.导包
import requests
# 2.获取session对象
session = requests.session()
# 3.请求验证码 让session对象记录cookies信息
url_verify = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify"
session.get(url_verify)
# 4.请求登录
url_login = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login"
data= {
                                "username": "13800138006",
                                "password": "123456",
                                "verify_code": "iqp7"
                                }
r = session.post(url=url_login,data=data)
print(r.json())
# 5.查询我的订单
url_order = "http://www.testingedu.com.cn:8000/Home/Order/order_list.html"
r = session.get(url_order)
print(r.text)