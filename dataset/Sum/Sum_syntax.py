def sum_array(arr):
    # Initialize a variable to hold the sum
    total = 0
    
    # Loop through the array and add up each element
    for num in arr:
        # Check if the value is a number
        if not isinstance(num, (int, float)):
            raise TypeError(f"Array element {num} is not a number.")
    total += num
    
    # Return the final sum
    return total
