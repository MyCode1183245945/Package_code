#  Chapter 9.1     Class     类

# 面向对象是最有效的软件编写方法之一，在面向对象编程中，你编写现实中的事物和情景的类，并基于这些类来创建对象。编写类时，你定义一大类对象都有的通用行为，基于类创建对象时，每个对象自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性.

# 创建 Dog 类
    # 根据DOG 类创建的每个实例都将存储名字和年龄，我们赋予了每条小狗蹲下（sit()）和打滚（roll_over()）的能力

class Dog():
    '一次模拟小狗简单的尝试'
    def __init__(self,name,age):
        '初始化属性 name ， age '
        self.name = name
        self.age = age

    def sit(self):
        '模拟小狗被命令蹲下'
        print(self.name.title() + ' ' + 'is now sitting.')

    def roll_over(self):
        '模拟小狗被命令打滚'
        print(self.name.title() + ' ' + 'rolled over' )

my_dog = Dog('willie',6)
your_dog = Dog('Lucy',3)
print('my dog name is '+my_dog.name.title() + '! ')  # 访问属性
print('my dog is  '+ str(my_dog.age) + ' yeas old! ')
my_dog.sit()               # 调用方法
my_dog.roll_over()


print('练习 ：Practice')
# 9-1 餐馆：创建一个名为 Restaurant 的类，其方法 __init__() 设置两个属性：restaurant_name 和 cuisine_type
     #创建一个名为 describe_restaurant() 的方法和一个名为 open_restaurant() 的方法，其中打印前述两项信息，而后者打印一条消息，指出餐馆正在营业
     #根据这类创建一个名为restaurant 的实例，分别打印其两个属性，在调用前述两个方法

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of this restaurant is '+ self.restaurant_name.title() + '!')
        print('The food is restaurant is ' + self.cuisine_type.title() + '!')
    def open_restaurant(self):
        print('The ' + self.restaurant_name.title() + ' is open as usual')


restaurant = Restaurant('Hunan restaurant','cantonese')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

















