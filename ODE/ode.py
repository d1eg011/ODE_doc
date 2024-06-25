"""Approximate the solution for ordinary differential equations at a future instant with information from past instants.

Modules exported by this package:

- `f`: function associated with the example differential equation.
- `euler`: One iteration of the Euler method applied to an ordinary differential equation.
- `rk2`: One iteration of the RK2 method applied to an ordinary differential equation.
- `rk4`: One iteration of the RK4 method applied to an ordinary differential equation.
"""

def func(x, t):
    """Function associated with the example differential equation.
    
    Examples:
        >>> func(1.0, 1.0)
        2.0

    Args:
        x (float): Dependent variable.
        t (float): Independent variable or time.

    Returns:
        (float): The sum operation of `x` and `t`. 
    """

    return x + t

def euler(f, x, t, h):
    """One iteration of the Euler method applied to an ordinary differential equation.

    Examples:
        >>> euler(func, 1.0, 1.0, 0.25)
        1.5

    Args:
        f: Function associated to the ordinary differential equation.
        x (float): Value of the dependent variable at the time `t`.
        t (float): Present time for the calculus of the dependent variable `x` in the next instant.
        h (float): Step that separates the time `t` from the next instant `t+h`.

    Returns:
        (float): The value of the dependent variable `x` in the time `t+h`. 
    """

    return x + h*f(x, t)

def rk2(f, x, t, h):
    """One iteration of the RK2 method applied to an ordinary differential equation.

    Examples:
        >>> rk2(func, 1.0, 1.0, 0.25)
        1.59375

    Args:
        f: Function associated to the ordinary differential equation.
        x (float): Value of the dependent variable at the time `t`.
        t (float): Present time for the calculus of the dependent variable `x` in the next instant.
        h (float): Step that separates the time `t` from the next instant `t+h`.

    Returns:
        (float): The value of the dependent variable `x` in the time `t+h` following the RK2 method. 
    """
    k1 = h * f(x, t)
    k2 = h * f(x + k1/2, t + h/2)

    return x + k2

def rk4(f, x, t, h):
    """One iteration of the RK4 method applied to an ordinary differential equation.

    Examples:
        >>> rk4(func, 1.0, 1.0, 0.25)
        1.60205078125

    Args:
        f: Function associated to the ordinary differential equation.
        x (float): Value of the dependent variable at the time `t`.
        t (float): Present time for the calculus of the dependent variable `x` in the next instant.
        h (float): Step that separates the time `t` from the next instant `t+h`.

    Returns:
        (float): The value of the dependent variable `x` in the time `t+h` following the RK4 method. 
    """
    k1 = h * f(x, t) 
    k2 = h * f(x + k1/2, t + h/2)
    k3 = h * f(x + k2/2, t + h/2)
    k4 = h * f(x + k3, t + h)

    return x + (k1+2*k2+2*k3+k4)/6
