import math

# Arrhenius equation constants
R = 8.314  # Gas constant (J/mol*K)

def reaction_rate(A, Ea, T):
    """
    Calculate reaction rate constant using Arrhenius equation
    """
    k = A * math.exp(-Ea / (R * T))
    return k


def main():
    print("Reaction Rate Simulator")

    A = float(input("Enter pre-exponential factor (A): "))
    Ea = float(input("Enter activation energy (J/mol): "))
    T = float(input("Enter temperature (Kelvin): "))

    k = reaction_rate(A, Ea, T)

    print("\nReaction rate constant k =", k)
    print("\n")

if __name__ == "__main__":
    main()