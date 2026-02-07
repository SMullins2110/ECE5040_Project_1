# ECE5040_Project_1
Project 1's goal is to implement the Finite-Difference Time-Domain (FDTD) method using a specific grid convention:
The Electric Field (E_z) is located at the center of the Yee cell, while the Magnetic Field (H_y) is located at the cell edges.

The project1.py file includes a script that utilizes NumPy and matplotlib.pyplot to create different scenarios,
where the Courant factor S, the source line Ez[nx // 4] = pulse, dielectric material, and deviations in ∆x are modified to evaluate edge cases.

Findings
-------------
- The Courant factor being set greater than 1.0 will result in an unstable plot where the y_axis "blows up". This happens due to the standard equation for the Courant factor stating that it must be less than or equal to 1.0. 

- Changes in the Soft vs Hard Source can create interactions that cause impedance mismatches and reflections / distortions specifically in the Hard Source case. A soft source allows for the reflected wave to pass through the original wave not causing distortion.

- The introduction of a dielectric slab (dielectric material) will begin to slow down the waveform and create partial reflections due to impedance mismatch. The wavelength will also change due to the dielectric material changing. In this specific case where e_r = 4, will create a wavelength that is half the original wavelength.

- Increasing the change in x will change the shape of the pulse. The pulse begins to disperse around dx = 0.5 where you can see significant reflections and the plot begins to become unstable. At dx = 1.0 we see that the y_axis (Electric field) becomes very large indicating an unstable waveform.
