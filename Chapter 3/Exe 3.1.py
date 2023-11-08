# Pay Cal with Overtime
# Input1: 45
# Input2: 10.50
# Expected Output: 498.75

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
  pay = (h * r)
elif h > 40:
  pay = (r * 1.5) * (h - 40) + (40 * r)
x = float(pay)
print(x)