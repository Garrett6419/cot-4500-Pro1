# cot-4500-Pro1
Programming Assignment 1 for COT 4500, Numerical Calculus

- Babylonian Approximation of sqrt(2)
- Bisection Method
- Fixed-Point Iteration
- Newton-Raphson Method

- Before testing anything make sure you have the necessary libraries installed. You can find these libraries in requirements.txt

- To use the assignemt_1.py, navigate to the src file and run: python main/assignment_1.py
- This will output the results of the following methods:

- Approximation of the square root of 2 using the Babylonian method
- Fixed-point iteration to find a fixed point of the function ( f(x) = \frac{x}{2} + 1 )
- Bisection method to find a root of the function ( f(x) = x^2 - 4 ) in the interval [0, 5]
- Newton-Raphson method to find a root of the function ( f(x) = x^2 - 4 )

- To use the test_assignment_1.py, navigate to the src file and run: python -m unittest discover -s test
- This will run all the test cases in test_assignment_1.py to test the functions in assignment_1.py