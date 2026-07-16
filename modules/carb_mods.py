"""
File: carb_mods.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    A module with carbonate speciation functions.
"""


import numpy as np
from scipy.optimize import root_scalar

def carb_spec_tot(tot):
    
    """
    Calculate pH and speciation given solute totals.

    Parameters
    ----------
    tot: ndarray or float
        total concentration of dissolved inorganic carbon (mol/kg)

    Returns
    -------
    dictionary
        concentrations of individual species (mol/kg)
    """
      
    # Set values for some constants
    # Stoichometry matrix
    #        | H2CO3*|  H+
    #        --------|----
    # HCO3-  |  -1   |  1
    # CO3-2  |  -1   |  2
    #   OH-  |   0   |  1
    sc = np.array([[-1, 1],
                   [-1, 2],
                   [ 0, 1]])
    
    # Equilibrium constant vector
    keq = 10**np.array([-6.3, -16.6, -14.0])

    # Define master species error function
    def residC(cH2CO3):
        """
        Residual of total inorganic carbon concentration
        for a given H2CO3* concentration
        """        

        # Define proton error function
        def residH(cH):
            """
            Residual of charge balance or proton condition for given 
            proton concentration cH.
            """        
            
            # Calculate concentrations of pH-dependent species
            conc = keq * cH2CO3**(-sc[:, 0]) / (cH**sc[:, 1])
            
            # Get charge balance
            return cH - np.sum(sc[:, 1] * conc)
        
        # Get H+ concentration
        cH = root_scalar(residH, bracket=[1E-14, 1], method='brentq').root

        # Species concentrations
        conc = keq * cH2CO3 * -sc[:, 0] / (cH**sc[:, 1])

        # Calculate error in total IC balance
        # Note that intermediate results cH and conc are returned here in addition to actual residual
        return tot - (cH2CO3 + np.sum(conc * -sc[:, 0])), cH, conc

    # Solve for H2CO3* concentration (mol/kg) 
    # Because residC() returns more than just residual, lambda function and indexing of result is needed
    cH2CO3 = root_scalar(lambda x: residC(x)[0], bracket=[1E-10, tot], method='brentq').root

    # Get associated cH and concentrations of all species
    resid, cH, conc = residC(cH2CO3)
    all_conc = np.concatenate(([cH2CO3, cH], conc))

    nms = ['H2CO3*', 'H+', 'HCO3-', 'CO3-2', 'OH-']
    res = dict(zip(nms, all_conc))

    # And return species concentrations (mol/kg)
    return res


