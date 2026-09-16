"""
Description:
    A free ammonia calculator function. Does not include corrections
    for non-ideal behavior; technically only accurate for very
    dilute solutions. 
"""

import numpy as np

def free_NH3(TAN, pH, pKa = 9.56):
    """
    Calculate free ammonia concentration (NH3 (aq)) from pH and TAN concentration.

    Parameters
    ----------
    TAN : float
        Total ammoniacal nitrogen (TAN) concentration (any concentration units)
    pH : float
        Solution pH
    pKa : float
        Acid dissociation constant for NH4+

    Returns
    -------
    float with free ammonia concentration in same units as TAN input
    """

    # Calculate H+ concentration from pH
    c_H = 10**(-pH)

    # And Ka
    Ka = 10**(-pKa)

    # Apply equation from text
    c_NH3 = TAN / (1 + c_H / Ka)

    # Return solution
    return c_NH3 


