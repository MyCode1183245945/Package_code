# 9-1 餐馆：创建一个名为 Restaurant 的类，其方法 __init__() 设置两个属性：restaurant_name 和 cuisine_type。
#   创建一个名为 describe_restaurant() 的方法和一个名为 open_restaurant() 的方法，其中打印前述两项信息，而后者打印一条消息，指出餐馆正在营业
#   根据这类创建一个名为restaurant 的实例，分别打印其两个属性，在调用前述两个方法
class Restayrant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of this restaurant is ' + self.restaurant_name + ','+ self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + ' we are open')

restaurant = Restayrant('湘菜馆','湖南口味')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 三家餐馆 : 根据你为完成练习 9-1 而编写的类创建三个实例，并对没个实例调用方法 describe_restaurant()。
restaurant1 = Restayrant('和平饭店','上海口味')
restaurant2 = Restayrant('煲仔饭','广东口味')
restaurant3 = Restayrant('关东煮','日本\n')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3 用户：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。
#   在类User 中定义一个名 为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
#   创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        message ='This user name is: '+  self.first_name  + self.last_name
        return message
    def greet_user(self):
        print('hello ' + self.first_name  + self.last_name + '!\n')

userName = User('隔壁','老王')
print(userName.describe_user())
userName.greet_user()




# 9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。
#   根据这个类创建一个名为restaurant 的实 例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
#   添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
#   添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就 餐人数。

class Restayrant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):     # 餐馆名字和口味
        print('The name of this restaurant is ' + self.restaurant_name + ','+ self.cuisine_type)

    def open_restaurant(self):      # 正营业
        print(self.restaurant_name + ' we are open')

    def count_number(self):    # 这家餐馆多少人就餐
        print('这家' + self.restaurant_name + '有' + str(self.number_served) + '人就餐过')

    def set_number_served(self,number):   # 修改属性的值
        self.number_served = number

    def increment_number_served(self,numbers):  # 通过方法进行递增
        self.number_served += numbers

restaurant = Restayrant('湘菜馆','湖南口味')
restaurant.count_number()
restaurant.number_served = 100
restaurant.count_number()
restaurant.set_number_served(200)
restaurant.count_number()
restaurant.increment_number_served(300)
restaurant.count_number()
print('\n')


# 9-5 尝试登录次数：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。
#   编写一个名为increment_login_attempts() 的方法， 它将属性login_attempts 的值加1。
#   再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
#   根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；
#   然后，调用方 法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts  = 0

    def describe_user(self):
        message ='This user name is: '+  self.first_name  + self.last_name
        return message
    def greet_user(self):
        print('hello ' + self.first_name  + self.last_name + '! 今天登陆 '+ str(self.login_attempts) + '次。')

    def increment_login_attempts(self,number=1):
        self.login_attempts +=number

    def reset_login_attempts(self):
        self.login_attempts = 0


userName = User('隔壁','老五')
userName.increment_login_attempts()
userName.increment_login_attempts(3)
userName.greet_user()
userName.reset_login_attempts()
userName.greet_user()
print('\n')
# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。
#   这两个版 本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
#   编写一个显示这些冰淇淋 的方法。创建一个IceCreamStand 实例，并调用这个方法。
class Restayrant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):     # 餐馆名字和口味
        print('The name of this restaurant is ' + self.restaurant_name + ','+ self.cuisine_type)

    def open_restaurant(self):      # 正营业
        print(self.restaurant_name + ' we are open')

    def count_number(self):    # 这家餐馆多少人就餐
        print('这家' + self.restaurant_name + '有' + str(self.number_served) + '人就餐过')

    def set_number_served(self,number):   # 修改属性的值
        self.number_served = number

    def increment_number_served(self,numbers):  # 通过方法进行递增
        self.number_served += numbers

class IceCreamStand(Restayrant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['草莓口味','苹果口味','牛奶口味']

    def Iceram_tastes(self):
        while self.flavors:
            Ice_cream = self.flavors.pop()
            print('本店冰淇淋口味有：'+ Ice_cream)



restaurant = IceCreamStand('湘菜馆','湖南口味')
restaurant.describe_restaurant()
restaurant.Iceram_tastes()

print('\n')
# 9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
#   添加一个名为privileges 的属性，用 于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。
#   编写一个名为show_privileges() 的方法，它 显示管理员的权限。创建一个Admin 实例，并调用这个方法。
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts  = 0

    def describe_user(self):
        message ='This user name is: '+  self.first_name  + self.last_name
        return message
    def greet_user(self):
        print('hello ' + self.first_name  + self.last_name + '! 今天登陆 '+ str(self.login_attempts) + '次。')

    def increment_login_attempts(self,number=1):
        self.login_attempts +=number

    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print('这是管理员权限 ')

userName = Admin('隔壁','老六')
userName.show_privileges()
print('\n')

# 9-8 权限 ：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。将方法show_privileges() 移到这 个类中。
#   在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts  = 0

    def describe_user(self):
        message ='This user name is: '+  self.first_name  + self.last_name
        return message
    def greet_user(self):
        print('hello ' + self.first_name  + self.last_name + '! 今天登陆 '+ str(self.login_attempts) + '次。')

    def increment_login_attempts(self,number=1):
        self.login_attempts +=number

    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges= ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print('这是管理员权限:')
        for a in self.privileges:
            print(a)

userName = Admin('隔壁','老王')
userName.privileges.show_privileges()

print('\n')
# 9-9 电瓶升级 电 ：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。
#   这个方法检查电瓶容量，如果它不是85，就将它 设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，
#   然后对电瓶进行升级，并再次调用get_range() 。你会看到这辆汽车的续航里程增 加了。

class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def fill_gas_tank(self):   # 汽车邮箱容量为50升
        print('The '+ self.model + 'fuel capacity is 50 litre')

    def get_descriptive_name(self):      # 打印汽车信息
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name

    def read_odometer(self):    # 打印汽车开了多少公里
        print('Tis car has ' + str(self.odometer_reading) + 'miles on it .')

    def update_odometer(self,mileage):         # 修改属性
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can roll back an odometer!')

    def increment_odometer(self, miles):    # 通过方法进行递增
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,mode,year):
        super(ElectricCar,self).__init__(make,mode,year)  # python 2.7 中的继承
        self.battery = Battery()

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size)+ ' -kwh battery ')

    def get_range(self):
        if self.battery_size ==70 :
            range = 240
        elif self.battery_size ==85:
            range = 270
        message = 'this car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size =85
        else:
            print('你容量已经是85了')


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()