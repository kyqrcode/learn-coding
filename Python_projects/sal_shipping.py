weight = float(input("Weight of the package: "))

ground_ship = 20.00
ground_ship_prem = 125.00
drone_ship = 0

if weight <= 2.0:
    ground_ship += (weight * 1.50)
    drone_ship += (weight * 4.50)
elif weight > 2.0 and weight <= 6.0:
    ground_ship += (weight * 3.00)
    drone_ship += (weight * 9.00)
elif weight > 6.0 and weight <= 10.0:
    ground_ship += (weight * 4.00)
    drone_ship += (weight * 12.00)
elif weight > 10.0:
    ground_ship += (weight * 4.75)
    drone_ship += (weight * 14.25)
else:
    print("Error weight!")

print("Ground shipping total charge: $" + str(ground_ship))
print("Ground Shipping Premium total charge: $" + str(ground_ship_prem))
print("Drone Shipping total charge: $" + str(drone_ship))