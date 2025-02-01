# assignment_1.py

# approximate sqrt(2)
def approximation_algorithm(x0, tol=1e-5):
    iter = 0
    diff = x0
    x = x0

    while (diff >= tol):
        iter += 1

        y = x

        x = (x / 2) + (1 / x)

        diff = abs(x - y)

    return x, iter


def bisection_method(func, a, b, tol=1e-5):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have different signs at a and b.")
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if func(midpoint) == 0:
            return midpoint  # FOUND IT FOUND IT
        elif func(a) * func(midpoint) < 0:
            b = midpoint  # Root is left
        else:
            a = midpoint  # Root is right
    return (a + b) / 2.0  # mission failed, try again.


def fixed_point_iteration(func, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = func(x)
        if abs(x_new - x) < tol:
            return x_new  # Converged to a fixed point
        if x_new == x:  # Check for non-convergence
            raise ValueError("Fixed-point iteration did not converge.")
        x = x_new
    raise ValueError("Fixed-point iteration did not converge.")


def newton_raphson(func, func_prime, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        if func_prime(x) == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - func(x) / func_prime(x)
        if abs(x_new - x) < tol:
            return x_new  # Converged to a root
        x = x_new
    raise ValueError("Newton-Raphson method did not converge.")


# Example usage of the algorithms
if __name__ == "__main__":
    # Example function for testing
    def example_func(x):
        return x**2 - 4  # Example function: x^2 - 4

    def example_func_prime(x):
        return 2 * x  # Derivative of the example function

    # Approximating the sqrt(2) starting at 1.5 using Babylonian method
    print("Approximation Algorithm Result:", approximation_algorithm(1.5))

    # Using fixed-point iteration to find a fixed point of the function x/2 + 1, starting at 1
    print("Fixed Point Iteration Result:", fixed_point_iteration(lambda x: x/2 + 1, 1))

    # Using the bisection method to find a root of x^2 - 4 in the interval [0, 5]
    print("Bisection Method Result:", bisection_method(example_func, 0, 5))

    # Using the Newton-Raphson method to find a root of the example function x^2 - 4, starting at 1
    print("Newton-Raphson Result:", newton_raphson(example_func, example_func_prime, 1))