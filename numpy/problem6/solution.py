import numpy as np
heights_input = []
for _ in range(6):
    heights_input.append(float(input()))
heights_array = np.array(heights_input).reshape(-1,1)
squeezed_heights = np.squeeze(heights_array)
current_height = squeezed_heights[-1]
projected_heights = []
for _ in range(5):
    current_height *= 1.10
    projected_heights.append(f"{current_height:.2f}")
print("Predicted height for ages 6 to 10:")
print(projected_heights)