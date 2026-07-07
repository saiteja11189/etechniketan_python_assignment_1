# 12. Create the following variables:
attendance = True
assignment_submitted = False

# a. Which operator should be applied between these variables to get a True?
# Operator: 'or' (since True or False is True)
result_a = attendance or assignment_submitted
print("a. Operator to get True between variables: 'or'")
print(f"   Result: attendance or assignment_submitted = {result_a}")

# b. Which operator should be applied between these variables to get a False?
# Operator: 'and' (since True and False is False)
result_b = attendance and assignment_submitted
print("b. Operator to get False between variables: 'and'")
print(f"   Result: attendance and assignment_submitted = {result_b}")

# c. Which operator should be applied to 'attendance' to get a False?
# Operator: 'not' (since not True is False)
result_c = not attendance
print("c. Operator to apply to attendance to get False: 'not'")
print(f"   Result: not attendance = {result_c}")
