"""
File: cool_pred.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    Application of the `cool_rk()` model function from the
    cooling_mods module.
"""

import cooling_mods as cm

preds = cm.cool(
    T_init=80, 
    T_air=20, 
    mass=300, 
    area=0.026, 
    h=75, 
    time_range=(0., 60 * 60), 
    dt = 5 * 60
)

print(preds)

