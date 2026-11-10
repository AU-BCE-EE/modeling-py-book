"""
File: ice_mods_var.py
Class: Modelling 2026
Author: Sasha D. hafner

Description:
    Module with single ice melting model that accepts time-variable air temperature.
"""

from scipy.interpolate import PchipInterpolator
from scipy.integrate import solve_ivp
import numpy as np

def meltv(
    mass_0,
    air_temp_dat,
    h, 
    times, 
    dens=920,
    temp_freeze=0,
    Hf=333000
):  

    """ 
    Dynamic model for heat transfer to a melting block of ice, with 
    disappearance of the ice over time. This version accepts time-
    variable air temperature.

    Parameters
    ----------
    mass_0 : float
        Initial mass of ice (kg) 
    air_temp_dat : DataFrame
        Air temperature over time as a Pandas DataFrame with columns `time` (s) and `temp` (deg. C)
    h : float
        Convection heat transfer coefficient (W/m2-K)
    times : list or tuple or array
        time in output (s) 
    dens : float
        Ice density (kg/m3)
    temp_freeze : float
        Freezing point (deg. C)
    Hf : float
        Heat of fusion (J/kg)

    Returns
    -------
    dictionary
        With elements 't' for time (s) and 'm' for ice mass remaining (kg)
 
    """

    # Make function for air temperature
    air_temp_func = PchipInterpolator(air_temp_dat.time, air_temp_dat.temp, extrapolate=False)
     
    # Define rates function
    def rates(t, mass_t):

        if mass_t < 0:
            mass_t = 0

        # Get current air temperature (deg. C)
        air_temp = air_temp_func(t)

        # Get current exposed upper area, assuming hemisphere
        area = 2 * np.pi * (3 * mass_t / (2 * np.pi * dens))**(2/3)

        # Heat flow (W)
        Q = area * h * (air_temp - temp_freeze)

        # Melting rate (kg/s)
        dmdt = -Q / Hf

        return dmdt

    res = solve_ivp(
        rates, 
        t_span = [min(times), max(times)], 
        y0 = [mass_0], 
        t_eval = times
    )

    # Calculate temperature for output as well
    air_temp_t = air_temp_func(times)

    # Return user-friendly dictionary as results object
    out = {
        'time': res.t, 
        'air_temp': air_temp_t,
        'ice_mass': res.y[0, :]
    }

    return out
