# 一次模拟小狗的简单尝试
# 一次模拟小狗的简单尝试


class Dog(object):
    def __init__(self, name='default', age=0):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " is now rolling over")


dog = Dog('yellow tiger', 1)
dog.sit()
dog.roll_over()


class Restaurant:
    def __init__(self, restaurant_name="df", cuisine_type=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name:" + self.restaurant_name.title() + '\n' +
              "type:" + str(self.cuisine_type))

    def open_restaurant(self):
        print("creating an instance of class restaurant")


class LittleDog(Dog):
    def __init__(self, name='df', age=0, color='yellow'):
        super().__init__(name, age)
        self.color = color

    def sit(self):
        print(self.name.title() + " is now sitting likely")


with open("pi.txt") as pi_txt:
    contents = pi_txt.read()
    print(contents)
    print('pwl')
