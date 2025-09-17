# Write a function that stores info about a car in a dictionary.
# Arguments should be make and model. And should accept arbitrary keyword arguments.
# Add two more arguments (features) to the car using the arbitrary keyword argument.

def make_car(make, model, **car_files):
    car_dict = {
        'make': make.title(),
        'model': model.title(),
    }

    for car_file, value in car_files.items():
        car_dict[car_file] = value

    return car_dict

car = make_car('toyota', 'camry',
               Color='midnight blue',
               Wheels_circumference=16)

print(car)
