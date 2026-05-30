from car_info import Car
while True:
    try:
        year_model = int(input("Enter a Year Model of Car:"))
        model = input("Enter a model of Car:")
        break

    except ValueError:
        print("Please enter a year model of Car")

my_car = Car(year_model,model)
print(my_car)