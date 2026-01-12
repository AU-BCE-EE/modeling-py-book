# Book topics
A list of chapter topics and summary of contents to guide writing

-------------------------------------------------------------------
# 0. Preface
-------------------------------------------------------------------
This book is designed for the course “Modelling” in the Bachelor programmes in Biotechnology and Chemical Engineering at the Department of Biological and Chemical Engineering, Aarhus University.
Its primary aim is to introduce students to heat and mass transfer modelling through examples and case studies closely connected to real challenges in biological and chemical engineering. 
The book emphasizes both the underlying physical principles and their practical implementation.
All computational examples are implemented using Python, enabling students to develop transferable skills in scientific programming while exploring key modelling concepts.

-------------------------------------------------------------------
# List of symbols
-------------------------------------------------------------------
Modeling is a broad field with many different applications and both language and symbols are surprisingly inconsistent.
We will try to be consistent with both.

-------------------------------------------------------------------
# 1. Introduction to modeling - concepts, terminology, classification
-------------------------------------------------------------------

## Brief intro
* What is a model?
* Uses of modeling
* Examples

## Types of models--model classification
Idea is to introduce different types of models and the important features through classification.
* Point of classification
* Categories are not exclusive!
* Conceptual, mathematical, computer (software)
* Analytical vs. numerical
* 1D (2D...) vs. 0D
* Lumped vs. distributed parameter
* Steady-state vs. dynamic

## Terms
* PDE
* ODE
* Steady-state
* Lumping
* Conservation (or balance) equations
* Constitutive equations
* Linking equations
* Governing equations
* State variables
* Indendependent variables
* Model parameters

-------------------------------------------------------------------
# 2. Model formulation - getting to a governing equation
-------------------------------------------------------------------
* Present, explain, and apply the basic steps
* Bring a single example (cooling coffee) through all parts

## Basic steps
1. Initial concepts and assumptions (boundary, state variables, sketches)
2. Balance/conservation equations
3. Constitutive equations (transfer or rate equations)
4. Linking equations
5. Spatial or other simplifications
6. Initial or boundary conditions
7. Governing equation
8. Analytical or numerical solution

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

Show how models are formulated (developed) by combining balance and constitutive equations, with help from linking equations, to get to the governing equation (GE).
Just for 0D model here.
Alternative is to find a complete GE and simplify--that approach is explained for 1D+ models in a following chapter.

-------------------------------------------------------------------
# 3. Solving and implementing models 
-------------------------------------------------------------------

## GE to code
* Lots of variation in exactly how to do this
* Numerical implementations can use separate balance and constiutive equations without even going to a single GE
* Single GE can always be basis for numerical or analytical solutions and implementations

## Numerical introduction: Euler's method
* Continue with coffee example
* Implement and explain
* Show effect of time step

## Higher-order methods: `solve_ivp()`
* Continue with coffee example
* Implement and explain

## Closed-form models
Introduce concept of closed-form (analytical) solution and apply in some steady-state examples.
Steady-state will be the main way we work with analytical models.
* Basic idea: start with GE, simplify and solve symbolically 
* Show general form of solution to first-order models
* Coffee example, comparison to numerical solutions
* Heat and mass transfer examples, implementation, and application

## Using Python modules
Introduce module-based modelling approach

Note: Spatial models will take some more work--see later chapter

-------------------------------------------------------------------
# 3. Introduction to heat transfer
-------------------------------------------------------------------
Present heat transfer essentials.
Include examples of heat flux and flow calculations.

## Intro
Introduce modes, mechanisms, and fundamental constitutive equations for heat transfer.
* Heat is a form of energy
* Temperature measures heat energy indirectly
* Modeling temperature and energy consumption or loss etc. means predicting rate of heat energy flow
* Flux versus flow and why
* Constitutive equations naturally describe flux
* Modes: operational ways we classify heat flow

## Advection - simple bulk flow
Include note on dispersion

## Conduction, Fourier's law, thermal conductivity
* Derivative form
* Difference form
* Thermal conductivity $k$ is a material property
* Takes place in solids and fluids (fluids = liquids and gases (vapors = gases that are mostly liquid at normal conditions, like water))
* Typical $k$ values  

## Convection and Newton's law of cooling
* Fundamental rate law or constitutive equation for convection has a dumb name!
* Overall heat transfer and $U$

## Example
Include all modes in a single lumped-parameter model

-------------------------------------------------------------------
# 4. Introduction to mass transfer
-------------------------------------------------------------------
Mass transfer essentials

## Advection
Include note on dispersion

## Fick's laws and diffusion
* Diffusivity $D$ depends on both diffusing species and what it is diffusing through
* Approximate ranges

## Convection

## Mass transfer coefficient approach

## Interphase mass transfer through an inter*f*ace

## Example
Dissolved oxygen transport and consumption

-------------------------------------------------------------------
# 6. Spatial models
-------------------------------------------------------------------

## Governing equations and coordinate systems
* Advection, diffusion, source terms
* Volumetric source terms vs boundary source terms

## Method of lines and descretization
* Discretize space keep derivative of time
* Different schemes for discretization

## Node vs cells
* Conceptual illustration of cells and nodes
* What does it mean at the boundaries?
* Node-based more efficient to program and run but harder to understand
* Cell-based easier to understand and verify
* Ultimately book favors one (node?) but either is fine

## Flux versus state variable
* Analogous to lumped-parameter models
* Flux-based means explicitly programming constitutive equations--more code but easier to understand
* State variable approach means implementing a single GE, and usually requires a bit of Python trickery for code efficiency

## Boundary conditions (BCs) 
* Types: dirictlet, neumann, robin
* Number needed
* Implementation: as part of a single GE (ghost points) or explicit (easier but more code)

## Implementation
Show implementation through examples 
* Start with small number of nodes/cells
* Include different implementation and boundary condition approaches

-------------------------------------------------------------------

-------------------------------------------------------------------
# Appendix. Derivatives and differential equations
-------------------------------------------------------------------
Not sure where to put this!
* Derivative is a fundamental component in modeling
* Rate of something over something over infintesimally small intervals (d = differential = very small change)
* Examples: 
    dT/dt = rate of change of temperature over time
    dT/dx = *gradient* in temperature over space
* ODEs
* PDES are *partial* deriviatves--the "partial" (or del) symbol implies that the variable on the top also depends on other variables
* Difference equations (do we use these at all?)

-------------------------------------------------------------------
# Appendix. Python style guide
-------------------------------------------------------------------
Brief summary of PEP8 guide based on examples.
