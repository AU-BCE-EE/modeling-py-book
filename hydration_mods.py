"""
File: hydration_mods.py

Author: Sasha D. Hafner

Class: Modelling 2026

Description:
    A simple kinetic model for carbon dioxide hydration.
"""

import numpy as np
from scipy.integrate import solve_ivp

def co2_hydration(cco2, ch2co3, rf, rr, times):
    """
    Dynamic model of dissolved carbon dioxide hydration.

    Parameters
    ----------
    c_co2 : float
        Initial dissolved carbon dioxide concentration (mol/kg)
    rf : float
        First-order forward reaction rate constant (1/s)
    rr : float
        First-order reverse reaction rate constant (1/s)
    times : array-like
        Times for evaluation

    Returns
    -------
    dictionary with times and concentrations 
    """

    # Define rates function
    def rates(t, conc):

        frate = conc[0] * rf
        rrate = conc[1] * rr
        dco2dt = - frate + rrate 
        dh2co3dt = - rrate + frate

        return [dco2dt, dh2co3dt]

    res = solve_ivp(
        rates, 
        t_span = [min(times), max(times)], 
        y0 = [cco2, ch2co3], 
        t_eval = times
    )

    # Return user-friendly results object (dictionary here)
    out = {
        "t": res.t, 
        "co2": res.y[0, :],
        "h2co3": res.y[1, :],
    }

    return out
