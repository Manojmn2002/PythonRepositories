def print_x_shape(size):
    if size % 2 == 0:
        print("Size must be an odd number.")
        return

    for i in range(size):
        for j in range(size):
            if j == i or j == size - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage:
n = 5 
print_x_shape(n)
