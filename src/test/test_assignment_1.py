# test_assignment_1.py

import unittest
import sys
import os

# Adjust the path to point to the 'main' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from assignment_1 import ( 
    approximation_algorithm,
    bisection_method,
    fixed_point_iteration,
    newton_raphson
)

class TestAssignment1(unittest.TestCase):

    def test_approximation_algorithm(self):
        # Test the approximation algorithm for sqrt(2)
        result, iterations = approximation_algorithm(1.5)
        self.assertAlmostEqual(result, 1.41421, places=5)  # Check if close to sqrt(2)
        self.assertGreater(iterations, 0)  # Ensure some iterations were performed

    def test_bisection_method(self):
        # Test the bisection method with a known root
        def func(x):
            return x**2 - 4  # Root at x = 2

        result = bisection_method(func, 0, 5)
        self.assertAlmostEqual(result, 2.0, places=2)  # Check if close to 2

    def test_fixed_point_iteration(self):
        # Test fixed-point iteration with a simple function
        def func(x):
            return x / 2 + 1  # Fixed point at x = 2

        result = fixed_point_iteration(func, 1)
        self.assertAlmostEqual(result, 2.0, places=2)  # Check if close to 2

    def test_newton_raphson(self):
        # Test Newton-Raphson method with a known root
        def func(x):
            return x**2 - 4  # Root at x = 2

        def func_prime(x):
            return 2 * x  # Derivative

        result = newton_raphson(func, func_prime, 1)
        self.assertAlmostEqual(result, 2.0, places=2)  # Check if close to 2

    def test_bisection_method_invalid(self):
        # Test bisection method with invalid input (same sign at endpoints)
        def func(x):
            return x**2 + 1  # No roots, always positive

        with self.assertRaises(ValueError):
            bisection_method(func, -1, 1)

    def test_fixed_point_iteration_invalid(self):
        # Test fixed-point iteration for non-convergence
        def func(x):
            return x + 1  # No fixed point

        with self.assertRaises(ValueError):
            fixed_point_iteration(func, 0)

    def test_newton_raphson_invalid(self):
        # Test Newton-Raphson with zero derivative
        def func(x):
            return x**3  # Root at x = 0

        def func_prime(x):
            return 3 * x**2  # Derivative is zero at x = 0

        with self.assertRaises(ValueError):
            newton_raphson(func, func_prime, 0)

if __name__ == '__main__':
    unittest.main()