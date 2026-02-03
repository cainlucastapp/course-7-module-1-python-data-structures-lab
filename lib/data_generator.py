# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    # Use a generator expression to filter students by major
    generator = (
        # Student tuple
        student
        # Loop through each student in the student_list
        for student in student_list
        # Only include students whose major matches the given major (case insensitive)
        if student[2].lower() == major.lower()
    )
    
    # Return the generator object
    return generator