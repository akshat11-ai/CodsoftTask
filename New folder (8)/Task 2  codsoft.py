# Function to calculate total marks, average percentage, and grade
def calculate_results(subject_marks):
    # Calculate total marks
    total_marks = sum(subject_marks)
    
    # Calculate average percentage
    num_subjects = len(subject_marks)
    average_percentage = total_marks / num_subjects
    
    # Grade Calculation based on average percentage
    if average_percentage >= 90:
        grade = 'A+'
    elif 80 <= average_percentage < 90:
        grade = 'A'
    elif 70 <= average_percentage < 80:
        grade = 'B'
    elif 60 <= average_percentage < 70:
        grade = 'C'
    elif 50 <= average_percentage < 60:
        grade = 'D'
    else:
        grade = 'F'
    
    # Return results
    return total_marks, average_percentage, grade

# Input: Ask the user to enter marks for each subject
subject_marks = []
num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_subjects):
    mark = float(input(f"Enter marks obtained in subject {i + 1}: "))
    subject_marks.append(mark)

# Calculate results
total_marks, average_percentage, grade = calculate_results(subject_marks)

# Display the results
print("\n--- Student Results ---")
print(f"Total Marks: {total_marks} out of {num_subjects * 100}")
print(f"Average Percentage: {average_percentage:.2f}%")
print(f"Grade: {grade}")
