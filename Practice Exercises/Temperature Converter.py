# Implement functions to convert temperature between Celsius and Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is {fahrenheit_temperature:.2f} Fahrenheit")

fahrenheit_temperature = 77
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is {celsius_temperature:.2f} Celsius")
