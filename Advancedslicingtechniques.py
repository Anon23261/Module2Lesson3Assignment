# Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 103, 104, 105, 106]

second_week_temperatures = temperatures[7:14]
print("Second week temperatures:", second_week_temperatures)

# Task 2: Extract
temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", temperatures_above_100)
