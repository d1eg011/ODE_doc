# Numerical methods to solve ODEs

## Type of problems to solve

This methods resolve ordinary diffential equations (ODEs) rule by a initial condition, such as:

$$
\frac{\text d x}{\text d t} = f(x, t) \quad \text{, where} \quad x(t=0)=x_{0}
$$

## Euler Method 

Is a simple Taylor expansion by a timestep **h** (which supposed to be small).  In this case the value of a funtion `x(t)` advanced in each timestep **h** as:    

$$
\boxed{x(t + h) = x(t) + h f(x,t)}
$$

The method holds an approximation error that has a linear dependece of **h** ($O(h)$), when the amount of timesteps taken in between the start and the end is defined as $(a +b) / h$.

The aplication of the method follows the next squeme:

- Starting point on $t = t_{0}$ and $x = x_{0}$.
- The times gets discretized for an equidistant timestep **h**, and it is identifed as $t_{i}$
- For each $t_{i}$ the function is calculated as: $x_{i} = x_{i-1} + h f(x_{i})$

## Runge-Kutta Methods

This are a family of numerical methods of different order that have a better approximation without taking into acount higther terms of Taylor's expansion.

### Second Order Runge-Kutta (RK2)

This methods uses the same line of expansion as Euler method but taking a midpoint, that is, insted of evaluating the derivate at $x= t+ h$, it is evaluated at $x = t+ h/2$. The expresion for $x(t+h)$ after the expansion is:

$$
\boxed{x(t + h) = x(t) + hf[x(t + h/2), t + h/2] + O(h^3)}
$$

The expansion at a midponit of $x(t)$ and $x(x +h)$ cancel the terms with $O(h^2)$; which changes the approximation error to the order of $O(h^{3})$,$, which is very benefitial computacionally.

To applied this method it's required to get the value in the midpoint $x(t + h/2)$ with the Euler method at a timestep **h/2** [$(x + h/2) = x(t) + \frac{h}{2}f(x,t)$], which implies the RK2 method equations can be written as:

* $k_{1} = hf(x,t),$
* $k_{2} = hf\left(x + \frac{k_{1}}{2},t + \frac{h}{2}\right)$
* $x(t + h) = x(t) + k_{2}$

### Fourth Order Runge-Kutta (RK4)

The equations for this orden are obtained through the same procedure as for RK2, but evaluating at four points between $x(t)$ and $x(x +h)$, leaving a approximation error of $O(h^5)$ and a global one of $O(h^4)$. The equations for RK4 are:

* $k_{1} = hf(x, t)$,
* $k_{2} = hf\left(x + \frac{k_{1}}{2}, t+\frac{h}2\right)$,
* $k_{3} = hf\left(x + \frac{k_{2}}{2}, t+\frac{h}2\right)$,
* $k_{4} = hf\left(x + k_{3}, t + h \right)$,
* $x(t+h) = x(t) + \frac{1}{6}(k_{1} + 2 k_{2} + 2k_{3} + k_{4})$.

This is the most commonly used method to solve ODEs, thanks to it's precision and ease programming.

## Documentation

For the documentation of each of this methods (see reference section), there's an example for the ODE:

$$
\frac{\text d x}{\text d t} = x + t \quad \text{, where} \quad x(t=0)=x_{0}
$$
