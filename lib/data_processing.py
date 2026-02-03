# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    # Extract student information from the tuple
    student_id = student[0]
    student_name = student[1]
    student_major = student[2]
    
    # Create the formatted string
    formatted_string = f"ID: {student_id} | Name: {student_name} | Major: {student_major}"
    
    # Return the formatted string
    return formatted_string


def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    # Loop through each student in the student_list
    for student in student_list:
        # Format the student data using the format_student_data function
        formatted_data = format_student_data(student)
        # Print the formatted student information
        print(formatted_data)