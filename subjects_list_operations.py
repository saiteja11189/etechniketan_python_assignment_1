# 11. Create a list named subjects containing: Python, SQL, Excel, Tableau
subjects = ["Python", "SQL", "Excel", "Tableau"]

# a. Display the complete list
print("a. Complete subject list:", subjects)

# b. Display the first subject and the last subject
print(f"b. First subject: {subjects[0]}, Last subject: {subjects[-1]}")

# c. Add one new subject between Python and SQL. Display the updated list
subjects.insert(1, "PowerBI")
print("c. Updated list after adding new subject between Python and SQL:", subjects)

# d. Delete Excel from the list and display the updated list
if "Excel" in subjects:
    subjects.remove("Excel")
print("d. Updated list after deleting Excel:", subjects)

# e. Copy the list into another list
new_subjects = subjects.copy()
print("e. Copied new list:", new_subjects)

# f. Sort the new list in ascending order
new_subjects.sort()
print("f. Sorted new list in ascending order:", new_subjects)

# g. Check if Excel is present in the list (using the 'in' operator)
is_excel_present = "Excel" in new_subjects
print("g. Is 'Excel' present in the new list?", is_excel_present)
