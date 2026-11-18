
# In-Memory Inventory Tracker using Dictionary Merging

# First inventory
inventory1 = {
    "Apple": 10,
    "Banana": 20,
    "Mango": 15
}

# Second inventory
inventory2 = {
    "Apple": 5,
    "Orange": 12,
    "Banana": 10
}

# Display first inventory
print("First Inventory:")
print(inventory1)

# Display second inventory
print("\nSecond Inventory:")
print(inventory2)

# Merge both dictionaries
merged_inventory = inventory1.copy()

for item, quantity in inventory2.items():
    if item in merged_inventory:
        merged_inventory[item] += quantity
    else:
        merged_inventory[item] = quantity

# Display merged inventory
print("\nUpdated Inventory:")
for item, quantity in merged_inventory.items():
    print(item, ":", quantity)

# Add a new product
merged_inventory["Grapes"] = 25

print("\nInventory After Adding New Product:")
print(merged_inventory)

# Search for a product
product = input("\nEnter product name to search: ")

if product in merged_inventory:
    print(product, "is available.")
    print("Quantity:", merged_inventory[product])
else:
    print(product, "is not available.")

# Total number of items
total = sum(merged_inventory.values())

print("\nTotal Inventory Quantity:", total)
