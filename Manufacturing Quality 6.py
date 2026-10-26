
# Manufacturing Quality Control Matrix

products = ("Product A", "Product B", "Product C")
batches = ("Batch 1", "Batch 2", "Batch 3")

# Production quantities for each product and batch
production = [
    [100, 200, 150],
    [120, 180, 200],
    [150, 250, 100]
]

# Defective units for each product and batch
defects = [
    [5, 12, 6],
    [15, 9, 20],
    [3, 30, 8]
]

threshold = 5.0

print("MANUFACTURING QUALITY CONTROL")
print("-----------------------------")

for i in range(len(products)):
    print("\nProduct:", products[i])

    for j in range(len(batches)):
        quantity = production[i][j]
        defective = defects[i][j]

        percentage = (defective / quantity) * 100

        print(batches[j])
        print("Production Quantity:", quantity)
        print("Defective Units:", defective)
        print("Defect Percentage:", round(percentage, 2), "%")

        if percentage > threshold:
            print("Status: Quality Threshold Exceeded")
        else:
            print("Status: Within Quality Limit")

# Identify batches exceeding the threshold
print("\n-----------------------------")
print("BATCHES EXCEEDING THRESHOLD")

for j in range(len(batches)):
    exceeded = False

    for i in range(len(products)):
        percentage = (defects[i][j] / production[i][j]) * 100

        if percentage > threshold:
            exceeded = True

    if exceeded:
        print(batches[j], "exceeds quality threshold")
