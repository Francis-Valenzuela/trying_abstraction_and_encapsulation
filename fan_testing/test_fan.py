from fan import Fan

# Speed = Max, Radius = 10, Color: Yellow, Status: On
fan_1 = Fan()
fan_1.set_speed(Fan.fast)
fan_1.set_radius(10)
fan_1.set_color('yellow')
fan_1.set_on(True)

fan_2 = Fan()
fan_2.set_speed(Fan.medium)
fan_2.set_radius(5)
fan_2.set_color('blue')
fan_2.set_on(False)

print("Fan 1:")
print("Speed:", fan_1.get__speed())
print("Radius:", fan_1.get__radius())
print("Color:", fan_1.get__color())
print("On:", fan_1.get__on())

# print("\nFan 2:")
# print("Speed:", fan_2.get__speed())
# print("Radius:", fan_2.get__radius())
# print("Color:", fan_2.get__color())
# print("On:", fan_2.get__on())