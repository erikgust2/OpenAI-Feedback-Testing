def celsius():
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = ((fahrenheit - 32) * 5) / 9
    print("The equivalent temperature in Celsius is", celsius)

    if(celsius > 32):
        print("It's hot!")
    elif(celsius < 0):
        print("It's cold!")
    else:
        print("It's just right!")

celsius()