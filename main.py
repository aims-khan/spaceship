print("Celsius to Fahrenheit Converter")
print("What do you want to convert? Celsius or Fahrenheit")
answer = input("Type your answer? celsius/fahrenheit ")


def celsius_fahrenheit():
    celsius = input("Enter celsius Value: ")
    fahrenheit = (int(celsius) * float(1.8)) + 32
    print(round(fahrenheit))
    # return fahrenheit


def fahrenheit_celsius():
    fahrenheit = input("Enter Fahrenheit Value: ")
    celsius = (int(fahrenheit) - 32) * 0.5556
    print(round(celsius))
    # return celsius


if answer == "celsius":
    celsius_fahrenheit()
elif answer == "fahrenheit":
    fahrenheit_celsius()
else:
    print("Invalid Value")