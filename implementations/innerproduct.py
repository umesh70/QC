import numpy as np
import math as m

def innerProd(state1, state2):
    """
    state1, state2: numpy arrays of size n
    
    Returns the inner product of state1 and state2
    """
    if state1.shape != state2.shape:
        return "Dimension unmatched, inner product not possible"
    
    # Calculate the conjugate of state1 and the dot product
    prodIn = np.dot(np.conjugate(state1), state2)
    
    return prodIn


# Example usage

state1 = np.array([5, 3j])
state2 = np.array([3, 5])
prod = innerProd(state1, state2)
print(prod)
