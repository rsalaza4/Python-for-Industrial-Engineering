### LINEAR PROGRAMMING - MINIMIZATION PROBLEM ###

# Example:

# min z = 10x1 + 15x2 + 25x3
# s.t.
# 1x1 + 1x2 + 1x3 >= 1000
# 1x1 - 2x2 + 0x3 >= 0
# 0x1 + 0x2 + 1x3 >= 340
#  x1 ,  x2 ,  x3 >= 0

# Import required libraries
import numpy as np
from scipy.optimize import linprog

# Set the inequality constraints matrix
# Note: the inequality constraints must be in the form of <=
A = np.array([[-1, -1, -1], [-1, 2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])

# Set the inequality constraints vector
b = np.array([-1000, 0, -340, 0, 0, 0])

# Set the coefficients of the linear objective function vector
c = np.array([10, 15, 25])

# Solve linear programming problem
res = linprog(c, A_ub=A, b_ub=b)

# Print results
print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)
