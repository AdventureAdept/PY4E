# Min Max Num Cal
# Inputs:
 
"""
7
 2
bob
10
4

"""

# Expected Outputs:

"""
 Invalid input
 Maximum is 10
 Minimum is 2

"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break    
    try:
        num = int(num)
        if largest is None or num > largest: 
            largest = num 
        if smallest is None or num < smallest: 
            smallest = num 
    except:
        print("Invalid input")

print("Maximum is", largest) 
print("Minimum is", smallest)