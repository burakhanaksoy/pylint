'''
Module for demo on PyLint

author: Burakhan Aksoy
date: 22-5-2021
'''

from math import sqrt
AVAILABLE_COLORS = ('pink', 'orange', 'aqua', 'yellow')


class Car:
    '''
    Car class, doesn't do much :))
    '''

    __slots__ = ('brand', 'type', 'year', 'color', 'on_sale',)

    def __init__(self, brand, type, year, color='white'):  # pylint: disable=redefined-builtin
        self.brand = brand
        self.type = type
        self.year = year
        self.color = color
        self.on_sale = False

    def ChangeColor(self, color):
        if not color in AVAILABLE_COLORS:
            print('Color is not available')
            return
        self.color = color

    def sell_My_CAR(self):
        self._on_sale_toggle()

    def _on_sale_toggle(self):
        if not self.on_sale:
            self.on_sale = True
            return
        self.on_sale = False
        return

    def drive_car(self):
        if not self.on_sale:
            print('Driving the car...')
        else:
            print("You cannot drive the car because it's on sale!")

    def random_method(self):
        self.gas = 0
        print(self.gas)


my_car = Car('BMW', 'Sedan', 2016)
my_car.ChangeColor('blue')
my_car.sell_My_CAR()
my_car.sell_My_CAR()
my_car.drive_car()
my_car.random_method()
