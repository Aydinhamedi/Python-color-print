# Python-color-print
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>

## Function Signature
```python
def print_Color(Input: str, colors: list, print_END: str = '\n', advanced_mode: bool = False):
```

## Parameters
- `Input` (str): The input string to be printed. In advanced mode, '~*' is used to separate different parts of the string to be printed in different colors.
- `colors` (list): A list of colors for the text. In non-advanced mode, only the first color in the list is used. In advanced mode, each color corresponds to a part of the input string separated by '~*'.
- `print_END` (str): The string appended after the final output, default is '\\n'.
- `advanced_mode` (bool): If True, enables advanced mode that allows multiple colors in one string. Default is False.

## Usage
In **normal mode**, you can print a string in a single color. For example:
```python
print_Color('Hello, World!', ['green']) 
```
This will print 'Hello, World!' in green.

In **advanced mode**, you can print different parts of a string in different colors. For example:
```python
print_Color('~*Hello in green~*Hello in red', ['green', 'red'], advanced_mode=True) 
```
This will print 'Hello in green' in green and 'Hello in red' in red.

## Special Characters
The '~*' characters are used as separators for different parts of the string that need to be printed in different colors when using advanced mode.

## Supported Colors
The colors that can be used are: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', and 'normal'. If an invalid color is provided, an error message will be printed.

Please note that this function uses ANSI escape codes for coloring, which may not work on all platforms or console types.
