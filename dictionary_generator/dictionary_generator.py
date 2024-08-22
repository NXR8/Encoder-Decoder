import itertools

# Define the character lists
list1 = ',./'
list2 = '!@#$%^&*()+=,./][}{'
list3 = '!@#$%^&*()+=,./123}45]67[890?{'
list4 = '1234567890'

# Generate all possible combinations using itertools.product
all_combinations = itertools.product(list1, list2, list3, list4)

# Open the file in write mode
with open('encod.txt', 'w') as f:
    for combination in all_combinations:
        # Join the tuple to form the encoded string
        encoded_string = ''.join(combination)
        # Write the encoded string to the file
        f.write(encoded_string + '\n')
        print(encoded_string)  # Optional: print to console
