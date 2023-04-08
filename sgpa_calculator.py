"""
Define a function to calculate the SGPA of a semester as per KTU regulation 2019 scheme. 

SGPA = Σ(Ci×GPi)/ΣCi , where ‘Ci’ is the credit assigned for a course and ‘GPi’ is the grade point for that course.
"""

def calculate_sgpa(grades):
    # Define the grade point mapping as per KTU regulation 2019
    grade_point_mapping = {
        'S': 10,
        'A+': 9,
        'A': 8.5,
        'B+': 8,
        'B': 7,
        'C+': 7.5,
        'C': 6,
        'P': 5.5,
        'F': 0,
        'FE': 0,
        'I': 0
    }
    
    total_credits = 0
    total_grade_points = 0
    
    # Calculate the total credits and grade points for all courses
    for course, (credits, grade) in grades.items():
        total_credits += credits
        total_grade_points += credits * grade_point_mapping.get(grade, 0)
    
    # Calculate the SGPA
    if total_credits > 0:
        sgpa = total_grade_points / total_credits
        return round(sgpa, 2)
    else:
        return 0.0


# Define the grades for each course as a dictionary
# The keys are the course names, and the values are tuples
# containing the number of credits and the grade received
grades = {
    'Maths': (4, 'A'),
    'Dbms': (3, 'B+'),
    'Flat': (2, 'C'),
    'Mm': (3, 'A+'),
    'Ms': (1, 'S')
}

# Calculate the SGPA for the given set of grades
sgpa = calculate_sgpa(grades)

# Print the SGPA
print("===============================")
print("\nThe SGPA Calculator")
print("_______________________________")
print("\nGiven credits and grades for each subject: \n'Maths': 4, 'A', \
    'Dbms': 3, 'B+', \
    'Flat': 2, 'C', \
    'Mm': 3, 'A+', \
    'Ms': 1, 'S'") 
print("\nThe calculated SGPA:", sgpa)
