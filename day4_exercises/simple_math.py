"""
A collection of simple math operations
"""

def simple_add(a,b):
    """Function to add two numbers"""
    return a+b

def simple_sub(a,b):
    """
    Function to substract two numbers:

    Parameters
    ----------
    a : float or int
        First number.
    b : float or int
        Second number.

    Returns
    -------
    Float or int
        a - b.

    """
    return a-b

def simple_mult(a,b):
    """Multiplication function:
    It takes two inputs, a and b, and multiplies a by b.
    """
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
