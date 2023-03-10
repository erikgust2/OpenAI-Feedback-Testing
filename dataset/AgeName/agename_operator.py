def greet_user():
    # Get the user's name and age
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    
    # Print a greeting message with the user's name and age
    print(f"Hello, {name}! You are {age} years old.")
    
    # Check the user's age and print a message based on it
    if age < 18:
        print("You're underage!")
    elif age >= 66:
        print("You're old!")
        years_retired = age + 66
        print(f"You've been retired for {years_retired} years.")
    else:
        years_left = 66 - age
        print(f"You have {years_left} years left until retirement.")
        print("You are an adult.")
