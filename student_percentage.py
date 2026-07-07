def main():
    # Accept inputs from the user
    student_name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")
    course_name = input("Enter Course Name: ")
    
    marks1 = float(input("Enter Marks in Subject 1: "))
    marks2 = float(input("Enter Marks in Subject 2: "))
    marks3 = float(input("Enter Marks in Subject 3: "))
    
    # Calculate total and percentage (assuming each subject is out of 100)
    total_marks = marks1 + marks2 + marks3
    max_marks = 300.0
    percentage = (total_marks / max_marks) * 100
    
    # Print student details and percentage
    print("\n--- Student Details Summary ---")
    print(f"Student Name : {student_name}")
    print(f"Age          : {age}")
    print(f"City         : {city}")
    print(f"Course Name  : {course_name}")
    print(f"Total Marks  : {total_marks} / {max_marks}")
    print(f"Percentage   : {percentage:.2f}%")

if __name__ == "__main__":
    main()
