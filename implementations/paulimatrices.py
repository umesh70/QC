import numpy as np

def pauliz():

    state0_ket= np.array([1,0])
    state0_bra = np.array([1,0])

    state0_out = np.outer(np.conjugate(state0_bra),state0_ket)
    
    state1_ket = np.array([0,1])
    state1_bra = np.array([0,1])
    state1_out = np.outer(np.conjugate(state1_bra),state1_ket)

    paulizOp = state0_out - state1_out
    
    return paulizOp


def applyPauliz(state):
    if len(state)!=2:
        raise ValueError("Qubit vector must be a 2D vector")
    
    operator = pauliz()
    return np.dot(operator,state)



state0= np.array([0,1])
result = applyPauliz(state0)

print(f"State before operator: {state0}")
print(f"State after operator: {result}")