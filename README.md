# Find the Most Common Value in a Dictionary

This repository contains a solution written in Python to the problem `Find the Most Common Value in a Dictionary`. This solution uses the concept of a frequency dictionary to store the frequency of each element in a collection then iterates through the given dictionary to calculate the most common value.

## Usage

To run the solution, open `main.py` and call the `find_most_common_value` function

```python
find_most_common_value(dictionary)
```

where `dictionary` is a dictionary type data structure. The function returns the most common value in the dictionary. If there is a tie, it returns the first value encountered with the highest frequency.

## Example

```python
find_most_common_value({'a': 5, 'b': 6, 'c': 7, 'd': 5, 'e': 7})
```

Returns `5`