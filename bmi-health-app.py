# BMI Health Advisor - Pre-Medical + CS Concept
# For UAE Scholarship Portfolio

def bmi_calculator():
    print("=== Health BMI Advisor (Medical + CS) ===")
    name = input("Patient Name: ")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (meters): "))
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        status = "Underweight - Need nutrition"
    elif bmi < 24.9:
        status = "Healthy - Perfect"
    elif bmi < 29.9:
        status = "Overweight - Exercise needed"
    else:
        status = "Obese - Consult doctor"
    
    print(f"\n--- Report for {name} ---")
    print(f"BMI: {bmi:.1f}")
    print(f"Status: {status}")
    
    # Saving data - basic file handling
    with open("health_records.txt", "a") as f:
        f.write(f"{name}, BMI: {bmi:.1f}, {status}\n")
    print("Record saved to health_records.txt")

bmi_calculator()
