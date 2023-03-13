def fahrenheit():
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("The equivalent temperature in Fahrenheit is", fahrenheit)

    if(fahrenheit > 90):
        print("It's hot!")
    elif(fahrenheit < 32):
        print("It's cold!")
    else:
        print("It's just right!")

fahrenheit()