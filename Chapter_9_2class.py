#  Chapter 9.2     Class     使用类和实例
# 你可以使用类模拟现实世界中很多前景，类编写好后，你的大部分时间都花在使用根据类创建的实例上，你需要执行一个重要的任务是修个实例的属性
#   ，也可以编写方法以特定的方式进行修改

print('car 类')

class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        '初始化汽车属性'
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        '返回整洁的描述信息'
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name()+'\n')

print('给属性指定默认值')
# 类中的没个属性都必须有初始值，哪怕这个值是0或者空字符串，如果设置默认时，在方法__init__() 内指定初始值是可以行的

class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        '初始化汽车属性'
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '返回整洁的描述信息'
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def red_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it \n')

my_new_car = Car('audi','a4','2016')
my_new_car.red_odometer()


print('修改属性的值,直接通过实例进行修改')
# 方法一 ： 直接通过实例进行修改
class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        '初始化汽车属性'
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '返回整洁的描述信息'
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def red_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it \n')

my_new_car = Car('audi','a4','2016')
my_new_car.odometer_reading = 66            # 直接修改属性的值
my_new_car.red_odometer()


# 方法二 ： 通过方法进行设置
print('修改属性的值,通过方法修改属性的值')
class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        '初始化汽车属性'
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '返回整洁的描述信息'
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def red_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it \n')

    def update_odometer(self,mileage):     # 通过方法修改属性的值
        self.odometer_reading = mileage

my_new_car = Car('audi','a4','2016')
my_new_car.update_odometer(67)
my_new_car.red_odometer()

# 方法三 ： 通过方法进行递增（增加特定的值）

class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        '初始化汽车属性'
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '返回整洁的描述信息'
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def red_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it \n')

    def update_odometer(self,mileage):     # 通过方法修改属性的值
        self.odometer_reading = mileage

    def increment_odmometer(self,miles):    # 通过方法进行递增
        self.odometer_reading += miles

my_new_car = Car('audi','a4','2016')    # 直接修改
my_new_car.odometer_reading = 6
my_new_car.red_odometer()

my_new_car.update_odometer(66)      # 方法修改
my_new_car.red_odometer()

my_new_car.increment_odmometer(10)   # 通过方法进行递增
my_new_car.red_odometer()