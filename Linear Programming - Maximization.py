# Import required libraries
import numpy as np
from scipy.optimize import linprog

# Set the inequality constraints matrix
A = np.array([[1, 0], [2, 3], [1, 1], [-1, 0], [0, -1]])

# Set the inequality constraints vector
b = np.array([16, 19, 8, 0, 0])

# Set the coefficients of the linear objective function vector
c = np.array([-5,-7]) # when maximizing, change the signs of the c vector coefficient!

# Solve linear programming probelm
res = linprog(c, A_ub=A, b_ub=b)

# Print results
print('Optimal value:', round(res.fun*-1,ndigits=2),
      '\nx values:',res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)
