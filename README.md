# Reaction Rate Simulator

## Aim
To calculate the reaction rate constant of a chemical reaction using the Arrhenius equation.

## Objective
This program estimates the reaction rate constant based on temperature, activation energy, and the pre-exponential factor. It demonstrates how temperature affects the speed of a chemical reaction.

## Theory
In chemical engineering, reaction kinetics studies the rate at which chemical reactions occur. One of the most important relations used to describe the temperature dependence of reaction rates is the Arrhenius equation.

The Arrhenius equation is expressed as:

k = A × e^(-Ea / RT)

Where:

- k = Reaction rate constant
- A = Pre-exponential factor (frequency factor)
- Ea = Activation energy (J/mol)
- R = Universal gas constant (8.314 J/mol·K)
- T = Absolute temperature (Kelvin)

The equation shows that as temperature increases, the exponential term increases, which leads to a higher reaction rate constant.

## Requirements

Python 3.x
No external libraries required (only built-in math library).

## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the program

## Test Values 

Inputs :

- Pre-exponential factor (A) = 10000000
- Activation energy (Ea) = 50000
- Temperature (T) = 350

Meaning :

- A = 1 × 10⁷ s⁻¹ (typical order of magnitude for reactions)
- Ea = 50 kJ/mol (moderate activation energy)
- T = 350 K (~77°C)

Expected Output :

- Reaction rate constant k ≈ 0.344
