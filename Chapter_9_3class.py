#  Chapter 9.3     Class    继承
# 如果你要编写的类是另一个现成类的特殊版本，可使用继承，一个类继承另一个一时，他将自动获得另一个类的所有属性和方法，原有的类成为父类
# 而新类称为子类，子类继承了其父类的所有属性和方法，同时可以自定义自己的属性和方法

print('子类的方法__init__()')
# 创建子类的实例时，首先要完成的任务是给父类的所有属性赋值，为此，子类的方法__init__() 需要父类施以援手.
# 模拟电动汽车，电动汽车是一种特殊汽车，因此我们可以在前面创建Car类的基础上创建新类ElectricCar,这样我们就只需要为电动汽车特有的属性和行为编写代码

class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

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

    def increment_odometer(self,miles):    # 通过方法进行递增
        self.odometer_reading += miles
class ElectricCar(Car):
    '电动汽车的独特之处'
    def __init__(self,make,model,year):
        '初始化父类属性'
        super().__init__(make,model,year)      # super() 是一个特殊函数，帮助Python将父类和子类关联起来
# python 2.7 中的继承
        # super(ElectricCar,self).__init__(make,model,year)

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())


print('\n给子类定义属性和方法')
# # 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。
# # 添加一个电动汽车的特有属性（电瓶） 储存电瓶容量，并编写一个打印电瓶属性的方法
#
class Car():
    '一次模拟汽车的简单尝试'
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

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

    def increment_odometer(self,miles):    # 通过方法进行递增
        self.odometer_reading += miles
class ElectricCar(Car):
    '电动汽车的独特之处'
    def __init__(self,make,model,year):
        '初始化父类属性,在初始化汽车的特有属性'
        super().__init__(make,model,year)      # super() 是一个特殊函数，帮助Python将父类和子类关联起来
        self.battery_size = 70

    def describe_battery(self):
        '打印一条描述电瓶容量的消息'
        print('this cars has '+ str(self.battery_size) + 'KW battery.\n')


my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


print('重写父类的方法')
# 对于父类的方法，只要它不符合子类模拟实物的行为，都可以对其进行重写，为此，可以在子类中定义一个这样的方法，即它与重写的父类方法同名，这样Python将不会考虑这个父类的方法
# 而只要关注你在子类中定义的相应方法
# 假设父类有个名为 fill_gas_tank() 的方法，他对电动汽车来说毫无意义，因此你可能要重写他
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
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model + '\n'
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
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

    def fill_gas_tank(self):
        '电动汽车没有邮箱'
        print("this car doesn't need a gas tank ! ")

my_tesla = ElectricCar('tesla','model s', 2016)
my_tesla.fill_gas_tank()
print(my_tesla.get_descriptive_name())


print('将实例用作属性')
# 用代码模拟实物时，你可能会发现在给类添加的细节越来越多，属性和方法清单以及文件都越来越长，在这种情况下，可能需要将类的一部分作为独立的类提取出来，你可以将大大型的类
#  拆分成多个协同工作的小类。

# 在不断给 ElectricCar 类添加细节时，可能会发现其中包含很多针对汽车电瓶的属性和方法，在这种情况下我们可以将这些属性和方法提取出来，放到另一个名为Battery 的类中
# 并将一个 Battery 实例用作 ElectricCar 类的一个属性
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


class Battery():
    def __init__(self,battery_size= 70):
        '初始化汽车电瓶属性'
        self.battery_size = battery_size
    def describe_battery(self):
        '打印一条描述电瓶容量的消息'
        print('This car has a ' + str(self.battery_size) + ' -KWH battery\n ')

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


print('下面给Battery类添加一个方法，它根据电瓶容量报告汽车的续航里程')
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


class Battery():
    def __init__(self,battery_size= 70):
        '初始化汽车电瓶属性'
        self.battery_size = battery_size
    def describe_battery(self):
        '打印一条描述电瓶容量的消息'
        print('This car has a ' + str(self.battery_size) + ' -KWH battery ')
    def get_range(self):
        '打印一条消息，指出电瓶的续航里程'
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'Tis car can go approximately ' + str(range)
        message += ' miles on full charge.'
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
