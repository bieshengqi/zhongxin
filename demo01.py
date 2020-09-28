"""
a = 1
while a > 0 :
    for i in range(35,0,-1):
        print("绿灯还有",i,"秒结束")
    for i in range(30,0,-1):
        print("红灯还有",i,"秒结束")
    for i in range(3,0,-1):
        print("黄灯还有",i,"秒结束")
"""

xingxi = {}

account = input ("请输入账号：")
password = input("请输入密码：")

if len(account) < 5 or len(account)>8:
    print("账号只能为5-8位")
elif len(password) < 6 or len(password)>12:
    print("密码只能为6-12位")
elif not account[0].islower():
    print("账号必须是小写开头")
else:
    xingxi[account]=password
    print("注册成功",xingxi)



