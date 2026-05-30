class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, on=False, radius=5.0, color="blue"):
        __speed = speed
        __on = on
        __radius = radius
        __color = color

    # accessors
    def get__speed(self):
        return self.__speed
    def get__on(self):
        return self.__on
    def get__radius(self):
        return self.__radius
    def get__color(self):
        return self.__color

    # mutators
    def set_speed(self, speed):
        self.__speed = speed
    def set_on(self, on):
        self.__on = on
    def set_radius(self, radius):
        self.__radius = radius
    def set_color(self, color):
        self.__color = color