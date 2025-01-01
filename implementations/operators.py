import numpy as np

#utilities
state0_ket= np.array([1,0])

state1_ket = np.array([0,1])

def identity():
    state0_out = np.outer(np.conjugate(state0_ket),state0_ket)
    
    state1_out = np.outer(np.conjugate(state1_ket),state1_ket)

    identityOp = state0_out + state1_out
    
    return identityOp

def pauliX():
    outbraket0 = np.outer(state0_ket, np.conjugate(state1_ket))
    outbraket1 = np.outer(state1_ket, np.conjugate(state0_ket))

    return outbraket0 + outbraket1

def pauliY():

    outBraKetNeg = np.outer(state0_ket,np.conjugate(state1_ket))
    outBraKetNeg = -1j*outBraKetNeg

    outBraKetPos = np.outer(state1_ket,np.conjugate(state0_ket))
    outBraKetPos = 1j*outBraKetPos

    return outBraKetNeg + outBraKetPos

def pauliZ():
    state0_out = np.outer(np.conjugate(state0_ket),state0_ket)
    
    state1_out = np.outer(np.conjugate(state1_ket),state1_ket)

    paulizOp = state0_out - state1_out
    return paulizOp


def applyOps(state):
    if len(state)!=2:
        raise ValueError("Qubit vector must be a 2D vector")
    
    identityop = identity()
    paulizOp = pauliZ()
    pauliyOp = pauliY()
    paulixOp = pauliX()
    
    return np.dot(identityop,state),np.dot(paulizOp,state),np.dot(pauliyOp,state),np.dot(paulixOp,state)



state0= np.array([0,1])
result = applyOps(state0)

print(f"Example state: {state0}")
print(f"State after Identity operator: {result[0]}")
print(f"State after Pauli-X operator: {result[3]}")
print(f"State after Pauli-Y operator: {result[2]}")
print(f"State after Pauli-Z operator: {result[1]}")