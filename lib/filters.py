# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    # Use list comprehension to filter students by major
    filtered_students = [
        # Add the entire student tuple to the new list
        student
        # Loop through each student in student_list
        for student in student_list
        # Only include students whose major matches the given input (case insensitive)
        if student[2].lower() == major.lower()
    ]
    
    # Return the filtered list
    return filtered_students