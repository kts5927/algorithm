import numpy as np

# Given constants for total conditions (stagnation conditions)
A = 0.000685468  # Area in m^2
Po = 7.76*10**6  # Total Pressure in Pa
To = 473  # Total Temperature in K
gamma = 1.261  # Specific heat ratio for air
R = 508.13  # Specific gas constant for air in J/(kg·K)

# Target mass flow rate
target_mass_flow_rate = 1.86  # kg/s

# Convergence criteria
tolerance = 0.0001  # Allowable error in mass flow rate
max_iterations = 100  # Maximum number of iterations

# Initial guess for Mach number
Mach = 0.5
step_size = 0.1  # Adjustment step for Mach number

# Iterative calculation
for iteration in range(max_iterations):
    # Calculate static temperature from total temperature using isentropic relation
    T = To / (1 + ((gamma - 1) / 2) * Mach**2)
    
    # Calculate static pressure from total pressure using isentropic relation
    P = Po / (1 + ((gamma - 1) / 2) * Mach**2) ** (gamma / (gamma - 1))
    
    # Calculate density using the ideal gas law
    rho = P / (R * T)
    
    # Calculate the current mass flow rate for the given Mach number
    m_dot = (A * P / (T ** 0.5)) * ((gamma / R) ** 0.5 * Mach) * (1 + ((gamma - 1) / 2) * Mach**2) ** (-(gamma + 1) / (2 * (gamma - 1)))
    
    # Calculate the error between the calculated and target mass flow rates
    error = target_mass_flow_rate - m_dot
    
    # Check for convergence
    if abs(error) < tolerance:
        break
    
    # Adjust Mach number based on error direction and magnitude
    Mach += step_size * error / abs(error)
    
    # Ensure Mach number does not go negative
    if Mach <= 0:
        Mach = 0.1

# Output the final results including Mach number, static pressure, static temperature, density, and mass flow rate
Mach, P, T, rho, m_dot, iteration
print()
