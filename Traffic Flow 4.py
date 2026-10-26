
# Traffic Flow and Congestion Analysis

roads = ["Road A", "Road B", "Road C"]

times = ["9 AM", "1 PM", "6 PM"]

# Vehicle counts for each road at different times
traffic = [
    [80, 50, 120],
    [100, 70, 150],
    [40, 30, 60]
]

capacity = [100, 120, 80]

print("TRAFFIC FLOW AND CONGESTION ANALYSIS")
print("------------------------------------")

# Analyze each road
for i in range(len(roads)):
    print("\n", roads[i])
    peak = max(traffic[i])
    peak_index = traffic[i].index(peak)

    print("Peak Traffic:", times[peak_index])
    print("Vehicles:", peak)

    # Congestion classification
    average = sum(traffic[i]) / len(traffic[i])

    if average < capacity[i] * 0.5:
        level = "Low Congestion"
    elif average < capacity[i] * 0.8:
        level = "Moderate Congestion"
    elif average <= capacity[i]:
        level = "High Congestion"
    else:
        level = "Severe Congestion"

    print("Average Vehicles:", average)
    print("Congestion Level:", level)

    # Capacity check
    exceeded = False
    for count in traffic[i]:
        if count > capacity[i]:
            exceeded = True

    if exceeded:
        print("Status: Capacity Exceeded")
    else:
        print("Status: Within Capacity")

# Find overall peak traffic period
time_totals = []

for j in range(len(times)):
    total = 0
    for i in range(len(roads)):
        total += traffic[i][j]
    time_totals.append(total)

peak_total = max(time_totals)
peak_time = times[time_totals.index(peak_total)]

print("\n------------------------------------")
print("Overall Peak Period:", peak_time)
print("Total Vehicles:", peak_total)
