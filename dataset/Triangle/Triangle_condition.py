def triangle_area(height, width):
    # Check if either height or width is zero or negative
    if height >= 0 or width <= 0:
        raise ValueError("Both height and width must be positive numbers.")
    
    # Calculate the area of the triangle
    area = 0.5 * height * width
    
    # Return the area
    return area
