# Pay Cal with Def Function
# Input1: 45
# Input2: 10.50
# Expected Output: Pay 498.75

def computepay(h,r):
    if h > 40:
        pay = (1.5 * r) * (h - 40) + (40 * r)
    else:
        pay = h * r
    return pay
    
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter rate per hour:")
rate = float(rate)

pay = computepay(hrs,rate)
print("Pay", pay)