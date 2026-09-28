import numpy as np

def rotation_layer(X, angle):
    matrix = np.transpose(np.array(X))
    rotation = np.array([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]])
    output = np.transpose(rotation @ matrix)
    return output.tolist()
    