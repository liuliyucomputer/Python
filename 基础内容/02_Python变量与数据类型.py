'''
Author: 刘礼宇 1605010842@qq.com
Date: 2025-07-15 02:34:55
LastEditors: 刘礼宇 1605010842@qq.com
LastEditTime: 2025-07-21 03:13:09
FilePath: \Python\基础内容\02_Python变量与数据类型.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 练习python文件的编写对应02_Python变量与数据类型.md
# 1.变量的基本概念
# 变量是用于存储数据的容器，变量名是变量的标识符，变量值是变量存储的数据。
# 变量名必须以字母或下划线开头，不能以数字开头，不能包含空格，不能使用Python的关键字。
# 变量名区分大小写。
# 变量名不能与Python的内置函数名相同。
# 变量名不能与Python的模块名相同。
# 变量名不能与Python的类名相同。
# 变量名不能与Python的函数名相同。
# 变量名不能与Python的变量名相同。
# 变量名不能与Python的常量名相同。
# 有效的变量名
name = "张三"
age_1 = 18
x = 100
y = 200
z = x + y
print(z)
print(x)
print(y)
# 多变量赋值
a, b, c = 1, 2, 3
a, b, c = c , b, a


# 私有变量的概念与用法
# 在Python中，变量名前加下划线有特殊含义：
# 单下划线 _var：表示“受保护变量”，约定仅类或模块内部使用，外部可访问但不推荐。
# 双下划线 __var：表示“私有变量”，会触发名称重整（name mangling），外部无法直接访问，推荐通过方法访问。
# 示例：
class Demo:
    def __init__(self1):
        self1._protected = "受保护的变量"
        self1.__private = "私有变量"
    def get_private(self1):
        return self1.__private
    
obj = Demo()
# 受保护变量可以访问l,但不推荐 
print(obj._protected)
# 私有变量无法直接访问
# print(obj.__private)
# 通过方法访问
# 在类内部定义方法时，第一个参数写self（代表实例本身）
# 在类外部调用方法时，不需要也不能手动传self，直接用obj.方法名()即可。
print(obj.get_private())

print(obj._Demo__private)  # 通过名称重整访问（不推荐）当你在类中定义以双下划线开头（但不以双下划线结尾）的变量（如__private），Python会自动将其“重命名”为_类名__变量名，以避免子类或外部直接访问，起到“伪私有”的作用。
age =   18  

big_number = 1_000_000_000  # 1_000_000_000 等价于 1000000000
print(big_number)
pi = 3.141592653589793  # 3.141592653589793
print(pi)
herght = 1.75  # 1.75
print(herght)
is_male = True  # True
print(is_male)
z=1+3j 
x=1j+3j
print(z, x ,z+x,z-x,z*x,z/x,z**x)
name="zhangsan" 
myname12='zhangsan1'
print(name,myname12,name+myname12)
address="beijing"
description="""这是一个多行
dada
字符串需要三个双引号"""
print(name,myname12,name*3)
firstchar=name[0]
print(firstchar)  
lastchar=name[-1]
print(lastchar)
print(name[1:3])
is_车子=True
是否有_轮子= False
print(f"是否有车子：,{is_车子}\n车上是否有轮子：{是否有_轮子}")
print(type(name))
print(type(name))
print(type(123))
print(type(a))

numbers=[1,2,3,4,5]
mixed = [1,"hello",True,3.132321,-0.3111111]
first = numbers[0]
last = numbers[-1]
subset = numbers[1:-1]
print(first,last,subset)
numbers.append(6)
numbers.insert(2,7)
numbers.remove(7)
numbers.pop(2) 
numbers[0] = '修改后的第一个数编号0'
numbers.append(7)
numbers.insert(1,7)
numbers.insert(2,7)
numbers.remove(7)
print(numbers)






print("删除最后一个元素")
numbers.pop()

print(numbers)
numbers.pop(0)
print(numbers)
numbers.pop(1)
print(numbers)
numbers.pop(-1)
print(numbers)
