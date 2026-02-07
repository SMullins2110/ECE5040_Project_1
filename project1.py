#Copyright (C) <2026> <Sean Mullins>
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulation Constants & Parameters ---
nx = 400  # Number of cells
nt = 1000
dx = 0.1
c0 = 299792458.0  # Speed of light in vacuum (m/s)
eps0 = 8.854187817e-12  # Permittivity of free space (F/m)
mu0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)

# epsr = np.ones(nx)  # Relative permittivity array
# epsr[200:] = 4.0 # Dielectric slab with εr = 4 starting from cell index 200

S = 0.5  # Courant number
dt = S * dx / c0  # Time step size

# ce = dt / (eps0 * epsr * dx)  # Update coefficient for electric field with material
ce = dt / (eps0 * dx)  # Update coefficient for electric field
ch = dt / (mu0 * dx)  # Update coefficient for magnetic field

# --- 2. Initialize Fields ---
# Ez at centers (nx), Hy at edges (nx + 1)
Ez = np.zeros(nx)
Hy = np.zeros(nx + 1)

# --- 3. Setup Visualization ---
plt.ion()  # Interactive mode on
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot(Ez, color='blue', lw=1.5)
ax.set_ylim([-1.2, 1.2])
ax.set_xlabel('Cell Index (i)')
ax.set_ylabel('Electric Field (Ez at center)')

# --- 4. Main Time-Stepping Loop ---
for tn in range(nt):

# Update Magnetic Field (Hy) at edges
# Hy[i] depends on Ez[i] and Ez[i-1]
    Hy[1:-1] += ch * (Ez[1:] - Ez[:-1])

# Store old Ez values for simple ABC
    ez_low_old = Ez[1]
    ez_high_old = Ez[-2]

# Update Electric Field (Ez) at centers
# Ez[i] depends on Hy[i+1] and Hy[i]
    Ez[:] += ce * (Hy[1:] - Hy[:-1])

# --- 5. Absorbing Boundary Conditions (Simple ABC) ---
    Ez[0] = ez_low_old
    Ez[-1] = ez_high_old

# --- 6. Soft Source Injection ---
    t0, sigma = 40, 12
    pulse = np.exp(-0.5 * ((tn - t0) / sigma) ** 2)
    Ez[nx // 4] += pulse

    if tn % 10 == 0:
        line.set_ydata(Ez)
    plt.draw()
    plt.pause(0.001)

plt.ioff()
plt.show()  
