"""
File: cool_pred.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    Application of the `cool_rk()` model function from the
    cooling_mods module. This version uses reload().
"""

# Original import of the model module
import cooling_mods as cm

# Get the reload() function from the importlib
# It is the only one we need so we just take that
from importlib import reload

# Use as needed (reload(pm) if module code is changed)
# This line below can be run multiple times in the same Python session
reload(pm)

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

