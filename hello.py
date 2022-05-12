""" Module docstring """
# Start virtual environment: .venv\Scripts\activate

import numpy as np
# pylint: disable=C0103
variable = 'World'
# variable = input("Enter your name: ")
print('Hello\n' + variable)

def my_strings():
    """ A function that outputs to the console

    The description can be over many lines.
    """
    message = f"variable is a {type(variable)}"
    print(message)

my_strings()

a = np.array([1, 2, 3, 4, 5, 6])
print(a[0])
