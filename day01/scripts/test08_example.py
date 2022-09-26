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
# 2.调用post
url_login = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login"
data = {
        "username": "13800138006",
        "password": "123456",
        "verify_code": "iqp7"
}
r = requests.post(url = url_login , data = data)
# 3.验证是否登录成功
print(r.json())
# 4.查询我的订单