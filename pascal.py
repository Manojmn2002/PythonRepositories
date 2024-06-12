def print_square_star(rows):
    for i in range(rows):
        for j in range(rows):
            print("* ", end="")
        print()

rows = 5
print_square_star(rows)