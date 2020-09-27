
"""
a = {"name":"花花","age":22,"like":"chil","motto":"星光不负赶路人"}
print(a["name"])

b=a.get("motto")
print (b)
a.update(age=23)
print(a)
"""
a = {
    "name":"none",
    "age":"none",
    "sex":"none"
    }

a.update(name=input("请输入姓名:"))
a.update(age=input("请输入年龄:"))
a.update(sex=input("请输入性别:"))
"""
a("name")=input("请输入姓名：")
a("age")=input("请输入年龄：")
a("sex")=input("请输入性别：")
"""
print("用户的信息为:",a)

