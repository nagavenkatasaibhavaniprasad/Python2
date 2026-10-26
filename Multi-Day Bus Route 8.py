
# Multi-Day Bus Route Performance Analysis

routes = ("Route A", "Route B", "Route C")
days = ("Monday", "Tuesday", "Wednesday")

# Passenger demand for each route over three days
passengers = [
    [90, 110, 130],
    [60, 70, 65],
    [140, 150, 160]
]

# Journey time in minutes
journey_time = [
    [40, 45, 50],
    [30, 35, 32],
    [55, 60, 65]
]

# Fuel usage in litres
fuel_usage = [
    [8, 9, 10],
    [5, 6, 5],
    [12, 13, 14]
]

# Bus capacity for each route
capacity = [120, 80, 140]

print("BUS ROUTE PERFORMANCE ANALYSIS")
print("--------------------------------")

for i in range(len(routes)):
    total_passengers = sum(passengers[i])
    total_time = sum(journey_time[i])
    total_fuel = sum(fuel_usage[i])

    average_passengers = total_passengers / len(days)
    average_time = total_time / len(days)
    average_fuel = total_fuel / len(days)

    print("\nRoute:", routes[i])
    print("Total Passengers:", total_passengers)
    print("Average Passengers:", round(average_passengers, 2))
    print("Average Journey Time:", round(average_time, 2), "minutes")
    print("Total Fuel Usage:", total_fuel, "litres")

    # Check route capacity
    overloaded = False

    for j in range(len(days)):
        if passengers[i][j] > capacity[i]:
            overloaded = True
            print(days[j], "- Overloaded")

    if overloaded:
        print("Capacity Status: Overloaded")
    else:
        print("Capacity Status: Within Capacity")

    # Calculate operating efficiency
    efficiency = total_passengers / total_fuel
    print("Fuel Efficiency:", round(efficiency, 2), "passengers per litre")

# Identify the most fuel-efficient route
efficiencies = []

for i in range(len(routes)):
    total_passengers = sum(passengers[i])
    total_fuel = sum(fuel_usage[i])
    efficiencies.append(total_passengers / total_fuel)

best_index = efficiencies.index(max(efficiencies))

print("\n--------------------------------")
print("Most Fuel-Efficient Route:", routes[best_index])
print("Efficiency:", round(efficiencies[best_index], 2),
      "passengers per litre")
