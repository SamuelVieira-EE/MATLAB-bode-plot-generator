import numpy as np

R = 1000 #resistance
C = 1e-6 #capacitance
num_points = 1000 #frequency points on the graph



tau = R * C
cutoff_freq = 1/(2*np.pi*tau) #formula for cutoff frequency

print("R =", R, "Ω")
print("C =", C*1e6, "μF")
print("Cutoff frequency =", cutoff_freq, "Hz")

#frequency range (logarithmic)
frequencies = np.logspace(-1, 5, num_points)  # 0.1 to 100000 rad/s

#magnitude and phase for each frequency
magnitudes = []
phases = []

for i in frequencies:
    # H(jw) = 1 / (jwτ + 1)
    H_real = 1 / (1 + (i * tau)**2)
    H_imag = -(i * tau) / (1 + (i * tau)**2)
    
    #magnitude in dB
    magnitude = 20 * np.log10(np.sqrt(H_real**2 + H_imag**2))
    
    #phase in degrees
    phase = np.arctan2(H_imag, H_real) * 180/np.pi
    
    magnitudes.append(magnitude)
    phases.append(phase)

#CSV file
data = np.column_stack([frequencies, magnitudes, phases])
np.savetxt('bode_data.csv', data, delimiter=',', header='frequency,magnitude,phase', comments='')


print("Created bode_data.csv")
print("Data points:", len(frequencies))
print("Frequency range:", frequencies[0], "to", frequencies[-1], "rad/s")