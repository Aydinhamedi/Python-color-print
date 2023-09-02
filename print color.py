#the print_Color func
def print_Color(Input: str, colors: list, print_END: str = '\n', advanced_mode: bool = False):
    """
    Prints colored text to the console. 

    Args:
        Input (str): The input string to be printed. In advanced mode, '~*' is used to separate different parts of the string to be printed in different colors.
        colors (list): A list of colors for the text. In non-advanced mode, only the first color in the list is used. In advanced mode, each color corresponds to a part of the input string separated by '~*'.
        print_END (str): The string appended after the final output, default is '\\n'.
        advanced_mode (bool): If True, enables advanced mode that allows multiple colors in one string. Default is False.

    Examples:
    ~~~python
        print_Color('Hello, World!', ['green']) 
        #Prints 'Hello, World!' in green.

        print_Color('~*Hello in green~*Hello in red', ['green', 'red'], advanced_mode=True) 
        # Prints 'Hello in green' in green and 'Hello in red' in red.
    Note:
        The colors that can be used are: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'normal'.
        If an invalid color is provided, an error message will be printed.
    """
    color_code = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'normal': '\033[0m'
    }

    if not advanced_mode:
        if colors[0] in color_code:
            print(color_code[colors[0]] + Input + '\033[0m', end=print_END)
        else:
            print("[\033[32mprint_Color\033[0m]\033[31mERROR: Invalid color input!!!\033[0m")
    else:
        substrings = Input.split('~*')
        if len(substrings) != len(colors) + 1:
            print("[\033[32mprint_Color\033[0m]\033[31mERROR: Number of colors and number of '~*' don't match!!!\033[0m")
        else:
            for sub_str, color in zip(substrings, ['normal'] + colors):
                if color in color_code:
                    print(color_code[color] + sub_str + '\033[0m', end='')
                else:
                    print(f"\n[\033[32mprint_Color\033[0m]\033[31mERROR: Invalid color!!!\033[33m the input color: '{color}' input list index: {colors.index(color)}\033[0m")
            print('', end=print_END)
#the func end




#example (Advanced_mode)
print('example (Advanced_mode): \n')
var = ['TEMP', 'TEST', 'DEBUG']

print_Color(f'{var} in red: ~*{var}~* in green: ~*{var}~*', colors=['red', 'normal', 'green', 'normal'], advanced_mode=True, print_END='|THE END \n\n')

#example (Simple)
print('example (Simple):\n')

print_Color('hello in red', colors=['red'])
