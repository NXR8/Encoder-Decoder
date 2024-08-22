# Dictionary Generator

This project generates all possible combinations of characters from predefined lists and saves them to a file. It uses Python's `itertools.product` to create combinations in a systematic manner.

## Overview

The provided script creates all possible permutations of characters from four lists. Each permutation is a combination of one character from each list, and the results are written to a text file.

## Code Explanation

### Imports

```python
import itertools
```
- **itertools**: A standard Python module providing functions to create iterators for efficient looping.

### Character Lists

```python
list1 = ',./'
list2 = '!@#$%^&*()+=,./][}{'
list3 = '!@#$%^&*()+=,./123}45]67[890?{'
list4 = '1234567890'
```
- These lists define the character sets used to generate combinations.

### Generating Combinations

```python
all_combinations = itertools.product(list1, list2, list3, list4)
```
- **itertools.product**: Generates the Cartesian product of the input iterables. This results in every possible combination of characters, where each combination consists of one character from each list.

### Writing to File

```python
with open('encod.txt', 'w') as f:
    for combination in all_combinations:
        encoded_string = ''.join(combination)
        f.write(encoded_string + '\n')
        print(encoded_string)  # Optional: print to console
```
- **File Handling**: Opens `encod.txt` for writing. Each combination is joined into a single string and written to the file. The string is also printed to the console (optional).

## Running the Script

Execute the script using Python:
```bash
python generate_combinations.py
```

The script will generate all possible character combinations and write them to `encod.txt` in the same directory.

## Notes

- **Performance Considerations**: Generating all possible combinations can produce a very large file depending on the number of characters in each list. Ensure you have sufficient disk space.
- **Customizing Lists**: You can modify `list1`, `list2`, `list3`, and `list4` to include different sets of characters as needed.

## License

This project is licensed under the MIT License.
