def is_magic_square(filename):
    with open(filename, 'r') as fh:
        # Read the dimension of the square
        dim = int(fh.readline().strip())

        # Read the square rows into a 2D list (as strings)
        magic_sq = []
        for _ in range(dim):
            row = fh.readline().strip().split()
            magic_sq.append(row)

    # Convert strings to integers for easier calculations
    for i in range(dim):
        for j in range(dim):
            magic_sq[i][j] = int(magic_sq[i][j])

    # Calculate the magic sum (sum of first row)
    magic_sum = sum(magic_sq[0])

    # Check each row sum
    for i in range(dim):
        if sum(magic_sq[i]) != magic_sum:
            return False

    # Check each column sum
    for j in range(dim):
        col_sum = 0
        for i in range(dim):
            col_sum += magic_sq[i][j]
        if col_sum != magic_sum:
            return False

    # Check main diagonal sum
    diag1_sum = 0
    for i in range(dim):
        diag1_sum += magic_sq[i][i]
    if diag1_sum != magic_sum:
        return False

    # Check secondary diagonal sum
    diag2_sum = 0
    for i in range(dim):
        diag2_sum += magic_sq[i][dim - 1 - i]
    if diag2_sum != magic_sum:
        return False

    # Check all numbers from 1 to n^2 appear exactly once
    expected_numbers = set(range(1, dim*dim + 1))
    actual_numbers = set()
    for i in range(dim):
        for j in range(dim):
            actual_numbers.add(magic_sq[i][j])

    if actual_numbers != expected_numbers:
        return False

    # If all checks pass, it's a magic square
    return True


# Example of running the check:
filename = "magic.dat"
if is_magic_square(filename):
    print("This is a magic square!")
else:
    print("This is NOT a magic square.")
