from car_info import Car
while True:
    try:
        year_model = int(input("Enter a Year Model of Car:"))
        model = input("Enter a model of Car:")
        break

    except ValueError:
        print("Please enter a year model of Car")

my_car = Car(year_model,model)

# accelerate 5 times
print("Accelerating:")
for accelerate in range(5):
    my_car.accelerate()
    print(my_car.get__speed())
# brake 5 times
print("Braking:")
for decelerate in range(5):
    my_car.brake()
    print(my_car.get__speed())

print(my_car)