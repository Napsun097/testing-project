def catAndMouse(x, y, z):
    # Calculate the distance from Cat A and Cat B to the Mouse
    distance_cat_a = abs(x - z)
    distance_cat_b = abs(y - z)
    
    # Determine the result based on the distances
    if distance_cat_a < distance_cat_b:
        return "Cat A"
    elif distance_cat_b < distance_cat_a:
        return "Cat B"
    else:
        return "Mouse C"

# Example usage:
x, y, z = map(int, input().split())  # Takes input as space-separated integers
print(catAndMouse(x, y, z))  # Output the result
