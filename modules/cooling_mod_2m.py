"""
File: cooling_mods_2m.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    A module with a single function implementing a numerical
    model for a cooling cup of coffee, including 2 modes of
    heat transfer from two locations.
"""

import numpy as np
from scipy.integrate import solve_ivp

def cool2m(T_init, T_air, mass, area_t, area_s, U_t, U_s, time_range, dt, cp=4.2):
    """
    Simulate coffee cooling using the RK45 method in `solve_ivp()`.

    Parameters
    ----------
    T_init : float
        Initial coffee temperature (deg. C)
    T_air : float
        Ambient air temperature (deg. C)
    mass : float
        Mass of coffee (g)
    area_t : float
        Upper surface area of the coffee (m2)
    area_s : float
        Surface area of the sides of the mug (m2)
    U_t : float
        Combined heat transfer coefficient from the top (W m-2 K-1)
    U_s : float
        Combined heat transfer coefficient from the sides (W m-2 K-1)
    time_range : tuple
        Start and end time (s), e.g. (0, 3600)
    dt : float
        Time step (s)
    cp : float, optional
        Specific heat capacity of coffee (J g-1 K-1), default 4.2

    Returns
    -------
    dict with keys 'times' (s) and 'T_coffee' (degC)
    """

    # Calculate constant, which does not change over time
    con_cool = (area_t * U_t + area_s + U_s) / (cp * mass)

    # Create an array of times
    times = np.arange(time_range[0], time_range[1] + dt, dt)

    # Define rates function
    def rates(t, T_current):
        return - con_cool * (T_current - T_air)

    # And use the RK45 method with solve_ivp() defaults
    res = solve_ivp(
        rates, 
        t_span=time_range, 
        y0=[T_init], 
        t_eval=times
    )

    # Return solution
    return {
        'times': res.t,
        'T_coffee': res.y[0, :],
    }


