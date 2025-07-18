# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle the number of rows
while row < size:
    # Inner for loop to handle the columns in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
