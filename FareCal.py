def calculate_fare(km, vehicle_type, hour):
    rates = {
        "Economy": 10,
        "Premium": 18,
        "SUV": 25
    }
    if vehicle_type not in rates:
        print("Service Not Available")
        return
    fare = km * rates[vehicle_type]
    if 17 <= hour <= 20:
        fare = fare * 1.5

    return fare

while True:
    print("\n1. Calculate Fare")
    print("2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        km = float(input("Enter distance (in km): "))
        vehicle_type = input("Enter vehicle type (Economy/Premium/SUV): ")
        vehicle_type = vehicle_type.upper()
        hour = int(input("Enter hour (0-23): "))
        result = calculate_fare(km, vehicle_type, hour)
        if result is not None:
            print("Total Fare:", result)
    elif choice == 2:
        print("Exiting...")
        break
    else:
        print("Invalid choice")