# Debug challenge 1

```{admonition} Challenge

The simple code listing below contains a number of bugs.  
Can you fix the code and help it to run?
```
**Hints:**
* Use a Python IDE such as`spyder` or `Visual Studio Code` it will help you debug.
* Read the Python interpreter output.  
* The errors reported can look confusing at first, but read them carefully and they will point you to the lines of code with problems.
* The `Spyder` IDE may give you some hints about formatting errors
* It can be useful to use `print()` to display intermediate calculations and variable values.
* Remember that `Spyder` has a variable viewer where you can look at the value of all variables created.  
* There might be multiple bugs!  When you fix one and try to run the code you might find another!

Have a go **yourself** and then watch our approach: 

* https://www.youtube.com/watch?v=XCuD59bYKx0


```python


def split_word_in_two(to_split):
"""
Returns string split into two parts

If the word's length is even the two parts have
equal number of characters

Params:
-------
to_split: str 
    the string to split int o
"""
length = len(to_spit)
half_length = length / 2

part1 = to_split[:half]
part2 = to_split[half:]

return part1, part2


def main():
"""
Tests the split_word_in_two function.
Input word = 'faster'
Expected output = ('fas', 'ter')
"""
word_to_split = 'faster'
result = split_word_in_two(word_to_split)
print('Part 1 = {0}; Part 2 = {1}'.format(result[0], result[1]))


if __name__ == "__main__":
   main()

```