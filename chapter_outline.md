# Book topics
A list of chapter topics and order to guide writing

## Introduction to modeling
Briefest intro with a couple examples perhaps.
* What is a model?
* Uses of modeling

## Types of models--model classification
Idea is to introduce different types of models and the important features through classification.
* Point of classification
* Categories are not exclusive!
* Analytical vs. numerical
* 1D (2D...) vs. 0D
* Lumped vs. distributed parameter
* Steady-state vs. dynamic

## A few important terms
Point is to give a first intro to some important model terms
* Conservation (or balance) equations
* Constitutive equations
* Linking equations
* Governing equations

## Conservation equations
Give a good solid introduction to mass and energy balances and even show how a simple "model" (or at least some system insights) can be developed from just a single conservation equation.
* A fundamental component of all models, whether realized or not
* Apply to energy and mass
* Can start with a "cookbook" formula:
    accumulation rate = rate in - rate out + rate gen - rate consumption
* But balances are flexible, each term can have multiple components and more terms may be added
* Typical to eliminate terms and perhaps rearrange for use in model
* Conservation equations apply to some volume or domain, typically (1) entire domainfor lumped parameter or 0D models or (2) a cell or node volume for 1D+ models or (3) an arbitrary "control volume" for symbolic math, i.e., developing a governing equation
* Include some examples: 
    - Balance equation as start of model dev
    - Balance equation that can be used alone for insight or a simple "model"

## Constitutive equations
Like balances, introduce reader to concept of constitutive equations and how they are a component of model dev.
* Why rates matter
* Example with Fourier's law
* Constitutive equations often have a derivative or difference on the RHS
* Constitutive equations covered in much more detail in a following chapter
* Constitutive equations depend on material properties and state variable

## Derivatives and differential equations
Not sure about having a separate chapter on this topic but seeing confusion from exam makes me think we should
* Derivative is a fundamental component in modeling
* Rate of something over something over infintesimally small intervals (d = differential = very small change)
* Examples: 
    dT/dt = rate of change of temperature over time
    dT/dx = *gradient* in temperature over space
* ODEs
* PDES are *partial* deriviatves--the "partial" (or del) symbol implies that the variable on the top also depends on other variables
* Difference equations (do we use these at all?)

## Heat transfer
Introduce modes, mechanisms, and fundamental constitutive equations for heat transfer.
* Heat is a form of energy
* Temperature measures heat energy indirectly
* Modeling temperature and energy consumption or loss etc. means predicting rate of heat energy flow
* Flux versus flow and why
* Constitutive equations naturally describe flux
* Modes: operational ways we classify heat flow

### Conduction, Fourier's law, thermal conductivity
* Derivative form
* Difference form
* Thermal conductivity $k$ is a material property
* Takes place in solids and fluids (fluids = liquids and gases (vapors = gases that are mostly liquid at normal conditions, like water))
* Typical $k$ values  

### Convection and Newton's law of cooling
* Fundamental rate law or constitutive equation for convection has a dumb name!

