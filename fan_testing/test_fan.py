from fan import Fan
# Fan 1: Fast, r = 10, yellow, on
fan1 = Fan()
fan1.set_speed(Fan.Fast)
fan1.set_radius(10)
fan1.set_color('Yellow')
fan1.set_on(True)
# Fan 2: Medium, r = 5, blue, off
fan2 = Fan()
fan2.set_speed(Fan.Medium)
fan2.set_radius(5)
fan2.set_color('Blue')
fan2.set_on(False)

print('Fan 1:')
print("Number:", fan1.get_speed())
print("Radius:", fan1.get_radius())
print("Color:", fan1.get_color())
print("On:", fan1.get_on())

print('\n')

print('Fan 2:')
print("Number:", fan2.get_speed())
print("Radius:", fan2.get_radius())
print("Color:", fan2.get_color())
print("On:", fan2.get_on())