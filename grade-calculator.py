# Grade Calculator - For Student Result System
# For UAE Scholarship Portfolio

def grade_calculator():
    print("=== Student Grade Calculator ===")
    name = input("Student Name: ")
    marks = float(input("Enter Marks out of 1100: "))
    
    percentage = (marks / 1100) * 100
    
    if percentage >= 90:
        grade = "A+ - Excellent (UAE Scholarship Level)"
    elif percentage >= 80:
        grade = "A - Very Good"
    elif percentage >= 70:
        grade = "B - Good"
    elif percentage >= 60:
        grade = "C - Pass"
    else:
        grade = "Needs Improvement"
    
    print(f"\n--- Result for {name} ---")
    print(f"Marks: {marks}/1100")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")

grade_calculator()
