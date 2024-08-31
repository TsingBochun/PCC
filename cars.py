

# Avoiding Index Errors When Working with Lists
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == "bnw":
        print(car.upper())
    else:
        print(car.title())