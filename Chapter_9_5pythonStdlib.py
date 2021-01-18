# 9.5 python 标准库
# Python 标准库是一组模块，安装Python都包含它。  下面来看下模块collections  中的一个类 OrderedDict

 # 记录被调查者参与调查的循序
from collections import OrderedDict

favorite_languages = OrderedDict()       #调用 OrderedDict（） 创建一个空的有序字典，并将其储存在 favorite_languages 中

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward']= 'ruby'
favorite_languages['phil'] = 'python'


for name,language in favorite_languages.items():
    print(name.title()+ "'s favorite language is " +
          language.title() + '.')
print('\n')
# 练习 practice
# 骰子骰 ：模块random 包含以各种方式生成随机数的函数，其中的randint() 返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：
import random
# x = random.randint(1,6)
# print(x)

# 创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数。
#   创建一个6面 的骰子，再掷10次。 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        number = random.randint(1,self.sides)
        return number

# number = Die()
# print(number.roll_die())
# number = Die(10)       # 创建一个10面的骰子，并将它们都掷10次
# for i in range(1,11):
#     print('第'+ str(i)+'次: '+ str(number.roll_die()))

# 生成从1到100，10位数的随机数列表
number = Die(100)
list1 = [number.roll_die() for i in range(1,11) ]
print(list1)

for i in range(1,len(list1)):
    for j in range(0,len(list1)-i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
print(list1)


