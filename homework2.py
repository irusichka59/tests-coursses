# Task 1 Write a program that can convert temperature from C to Fahrenheit and Kelvin
def temperature(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    print(fahrenheit, kelvin)


input_celsius = float(input("input celsius:"))

temperature(input_celsius)
