users = [("Alice", 25), ("Bob", 15)]

for name, age in users:
    activity = "driving" if age >= 18 else "school"
    print(f"{name} did {activity}")
