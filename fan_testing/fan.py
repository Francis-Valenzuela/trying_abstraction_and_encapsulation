class Fan:
    Slow = 1
    Medium = 2
    Fast = 3

    def __init__(self, speed=Slow, radius=5, color="blue", on=False):

        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_on(self):
        return self.__on
    def set_on(self, on):
        self.__on = on

    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius

