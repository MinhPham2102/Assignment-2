from abc import ABC, abstractmethod

class Bubble_Tea(ABC):
    def __init__(self, name, size, level_of_ice, level_of_sugar, type_of_tea, type_of_topping, price):
        self.__name = name 
        self.__size = size 
        self.__level_of_ice = level_of_ice
        self.__level_of_sugar = level_of_sugar
        self.__type_of_tea = type_of_tea
        self.__type_of_topping = type_of_topping
        self.__price = price


    @abstractmethod
    def calculate_price(self):
        pass



