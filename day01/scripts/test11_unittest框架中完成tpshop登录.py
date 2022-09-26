"""
目标：unitest框架中完成登录tpshop的领路
案例数据：
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
# 1.导包 unittest requests
import unittest
import requests


# 2.新建测试类-->unittest.TestCase
class TestLogin(unittest.TestCase):
    # 3.setUp
    def setUp(self):
        # 获取session对象
        self.session = requests.session()
        # 登录url
        self.url_login = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login"
        # 验证码url
        self.url_verify = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=verify"

        pass

    # 4.tearDown
    def tearDown(self):
        # 关闭session
        self.session.close()
        pass

    # case
    # 5.登录成功
    def test_login_success(self):
        # 请求验证码----->获取cookies
        self.session.get(self.url_verify)
        # 请求登录
        data = {
            "username": "13800138006",
            "password": "123456",
            "verify_code": "iqp7"
        }
        r = self.session.post(self.url_login, data=data)
        # 断言
        try:
            self.assertEqual("登陆成功", r.json()['msg'])
        except AttributeError as e:
            print(e)

    # 6.登录失败，账号不存在
    def test_username_not_exist(self):
        # 请求验证码----->获取cookies
        self.session.get(self.url_verify)
        # 请求登录
        data = {
            "username": "138001380066",
            "password": "123456",
            "verify_code": "iqp7"
        }
        r = self.session.post(self.url_login, data=data)
        # 断言
        try:
            self.assertEqual("账号不存在!", r.json()['msg'])
        except AttributeError as e:
            print(e)

    # 7.登录失败，密码错误
    def test_password_error(self):
        self.session.get(self.url_verify)
        # 请求登录
        data = {
            "username": "13800138006",
            "password": "1234567",
            "verify_code": "iqp7"
        }
        r = self.session.post(self.url_login, data=data)
        # 断言
        try:
            self.assertEqual("密码错误!", r.json()['msg'])
        except AttributeError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
