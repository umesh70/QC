import numpy as np
import math as m

# inner product on two different state vectors
"""
If each element of a set of vectors is normalized and the elements are orthogonal
with respect to each other, we say the set is orthonormal

when the inner product of a state vector with itself is 1,then its a normalized 
and when the inner product of two state vectors is 0 then state vectors are orthogonal

"""
def innerProd(state1, state2):

    
    if state1.shape != state2.shape:
        return "Dimension unmatched, inner product not possible"
    
    # Calculate the conjugate of state1 and the dot product
    prodIn = np.vdot(np.conjugate(state1), state2)
    
    return prodIn

def calNorm(state):
    # inner product of state vector with itself
    normstate = np.vdot(np.conjugate(state),state)
    # sqaure root to calculate the norm of the state vector
    norm = np.sqrt(normstate)

    #check if the state is normal or not
    ifNorm = np.isclose(norm,1.00)
    if not ifNorm:
        normfinal = state/norm
        verification = np.abs(np.vdot(normfinal, normfinal))
        return normfinal, verification
    return norm
# Example usage

state1 = np.array([0,1])
state2 = np.array([1,1j])

prod = innerProd(state1, state2)
result = calNorm(prod)
print(result)
if isinstance(result,tuple):
    norm,verification = result
    print("State is not normal")
    print(prod)
    print(f"Normalized state {norm}")
    print(f"Verification of norm (should be 1): {verification}")
    
else:
    norm = calNorm(prod)
    print("normalized state")
    print(f"Inner product between {state2} and {state2}: {prod}")
    print(f"Norm of the inner product between the states: {norm}")


