import numpy as np

def linspace(start, stop, n: int) -> np.ndarray:
    """n evenly spaced values from start to stop inclusive."""
    if n == 1:
        return np.array([start])
    step = (stop - start)/(n-1)
    step_multiplier = np.arange(n)
    output = np.ones(n)*start + step_multiplier*step
    return output
