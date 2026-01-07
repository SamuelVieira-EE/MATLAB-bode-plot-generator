import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('bode_data.csv', delimiter=',', skiprows=1)

frequency = data[:, 0]
magnitude = data[:, 1]
phase = data[:, 2]



#cutoff frequency
idx_3db = np.argmin(np.abs(magnitude + 3)) #the -3dB cutoff point is what we are looking for
cutoff_freq = frequency[idx_3db] #at cutoff signal is reduced by half power or -3db

print("Cutoff frequency:", cutoff_freq, "rad/s")
print("Phase at cutoff:", phase[idx_3db], "degrees")

#plot
plt.figure(figsize=(10, 8))

#the parameters for the top graph (magnitude)
plt.subplot(2, 1, 1)
plt.semilogx(frequency, magnitude, 'b-', linewidth=2)
plt.axhline(-3, color='r', linestyle='--', label='-3dB')
plt.axvline(cutoff_freq, color='g', linestyle='--')
plt.plot(cutoff_freq, -3, 'ro', markersize=10)
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot')
plt.grid(True)
plt.legend()

#the parameters for the bottom graph graph phase
plt.subplot(2, 1, 2)
plt.semilogx(frequency, phase, 'r-', linewidth=2)
plt.axhline(-45, color='b', linestyle='--', label='-45°')
plt.axvline(cutoff_freq, color='g', linestyle='--')
plt.plot(cutoff_freq, -45, 'bo', markersize=10)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('bode_plot.png')
plt.show()
