def print_reverse_pascal(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i, 0, -1):
            print(f"* ", end="")
        print()
rows = 5
print_reverse_pascal(rows)