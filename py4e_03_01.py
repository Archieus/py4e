#Inputs : hrs = 45, rate = 10.5
hrs = input("Enter Hours:")
rate = input("Hourly Rate:")
h = float(hrs)
r = float(rate)

if h > 40:
    regular = 40*r
    timehalf = (h-40)*(r*1.5)
    print(regular + timehalf)
else:
    print(h*r)
    
