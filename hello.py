# Start virtual environment: .venv\Scripts\activate

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
