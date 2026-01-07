# Bode Plot Generator

Generates bode plots for an RC low-pass filter.

## What it does
Creates magnitude and phase plots to show how a filter works with different frequencies.

## Transfer Function
Example function for demonstration
H(s) = 1 / (τs + 1) or H(jω) = 1 / (jωτ + 1) (frequency domain)

Where τ = RC (time constant)

**This has:**
- 1 zero at s = 0
- 1 pole at s = -1/τ

## Example
With R = 1000Ω and C = 1μF:
- Cutoff frequency = 159.15 Hz
- At cutoff: magnitude = -3dB, phase = -45°

## How to use

1. Install requirements:
```
pip install -r requirements.txt
```

2. Generate data:
```
python Bode_Plot_Graph.py
```

3. Plot results:
```
python test.py
```

## Change parameters
Edit `Bode_Plot_Graph.py`:
```python
R = 1000    # Change resistance
C = 1e-6    # Change capacitance
```

## Output
- `bode_data.csv` - Raw frequency response data
- `bode_plot.png` - Bode plot image
