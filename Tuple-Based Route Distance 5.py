
# Tuple-Based Route Distance Analysis

import math

# Store geographical coordinates as tuples (x, y)
points = [
    (0, 0),
    (3, 4),
    (6, 8),
    (12, 8),
    (15, 12)
]

distances = []

print("ROUTE DISTANCE ANALYSIS")
print("-----------------------")

# Calculate distances between successive points
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    distances.append(distance)

    print("Segment", i + 1, ":", points[i], "to", points[i + 1])
    print("Distance:", round(distance, 2))

# Identify the longest route segment
longest = max(distances)
index = distances.index(longest)

print("-----------------------")
print("Longest Route Segment:", index + 1)
print("Longest Distance:", round(longest, 2))
print("Total Route Distance:", round(sum(distances), 2))
