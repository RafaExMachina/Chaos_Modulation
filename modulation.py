# this module will be imported in the into your flowgraph

import numpy as np
import random

def skewTent(alfa, Npoints):
    """
    Generates a chaotic signal using the skew tent map.
    
    Parameters:
    - alfa: A parameter that controls the shape of the skew tent map.
    - Npoints: The number of points in the generated signal.
    
    Returns:
    A list of Npoints values representing the chaotic signal.
    """
    x = [0] * Npoints
    # Initialize the first point with a random value between -1 and 1
    x[0] = random.uniform(0, 1) * 2 - 1
    
    for i in range(Npoints - 1):
        
        if (x[i] < alfa):
            x[i + 1] = (2 / (alfa + 1)) * x[i] + ((1 - alfa) / (alfa + 1))
        
        elif (x[i] >= alfa):
            x[i + 1] = (2 / (alfa - 1)) * x[i] - ((alfa + 1) / (alfa - 1))
    return x[:Npoints]

##########################################################################

def CSK(nbits, alfa, BitSym):
    """
    Modulates a signal using Chaotic Shift Keying (CSK) with n bits.
    
    Parameters:
    - nbits: The number of bits to modulate.
    - alfa: A parameter used in the chaotic signal generation.
    - BitSym: The number of points in the chaotic signal per bit.
    
    Returns:
    The modulated signal as an array.
    """
    # Generate a sequence of bits (with values -1 or 1)
    bits = 2 * np.random.randint(2, size=nbits) - 1
    NumSymbols = bits.size
    # Generate a chaotic signal with a length based on the number of bits and BitSym
    chaoticSignal = skewTent(alfa, BitSym * NumSymbols)
    # Create a pulsed signal by repeating each bit BitSym times
    pulsedSignal = np.kron(bits, np.ones(BitSym))
    # Modulate the chaotic signal with the pulsed signal
    return chaoticSignal * pulsedSignal 

##########################################################################

def COOK(nbits, alfa, BitSym):
    """
    Modulates a signal using Chaotic On-Off Keying (COOK) with n bits.
    
    Parameters:
    - nbits: The number of bits to modulate.
    - alfa: A parameter used in the chaotic signal generation.
    - BitSym: The number of points in the chaotic signal per bit.
    
    Returns:
    The modulated signal as an array.
    """
    # Generate a sequence of bits (with values 0 or 1)
    bits =  np.random.randint(2, size=nbits) 
    NumSymbols = bits.size
    # Generate a chaotic signal with a length based on the number of bits and BitSym
    chaoticSignal = skewTent(alfa, BitSym * NumSymbols)
    # Create a pulsed signal by repeating each bit BitSym times
    pulsedSignal = np.kron(bits, np.ones(BitSym))
    # Modulate the chaotic signal with the pulsed signal
    return chaoticSignal * pulsedSignal 