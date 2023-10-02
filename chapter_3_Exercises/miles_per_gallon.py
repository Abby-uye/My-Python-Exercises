miles = 0
gallons = 0
stopper = 0
total_miles = 0
total_gallons = 0
while stopper != -1:
    gallons = float(input("Enter the gallons used :"))
    miles = float(input("Enter the miles you've driven:"))
    per_trip = miles / gallons
    print("The miles per gallon for each trip is", per_trip)
    total_gallons += gallons
    total_miles += miles
    stopper = int(input("Enter -1 to stop"))
combined_trip = total_miles / total_gallons
print("The combined miles per gallon is ", combined_trip)
