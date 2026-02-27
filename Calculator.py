num_1 = float(input("Enter 1st no: "))
num_2 = float(input("Enter 2nd no: "))

print("ARTHIMATIC OPERATIONS")
print()
print(f"Sum of the no.s is:",{num_1+num_2})
print(f"Difference of the no.s is:",{num_1-num_2})
print(f"Product of the no.s is:",{num_1*num_2})
if num_2 == 0:
    print("Cannot divide by zero")
else:
    print(f"Division of the no.s is:",{num_1/num_2})
    print(f"Modulus of the no.s is:",{num_1%num_2})
print(f"sq of 1st no.s is:",{num_1**2})
print()
print("COMPARISON CHECK")
print()

if num_1>num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1<num_2:
    print(f"{num_2} is greater than {num_1}")
else:    print(f"{num_1} and {num_2} are equal")
print()
print("LOGICAL SCENERIOS")
print()
if num_1>0 and num_2>0:
    print("Both the no.s are positive")
print()
if num_1>100 or num_2>100:
    print("At least one of the no.s is greater than 100")
print()
if num_2==0:
    print("Cannot divide by zero")
print()

    