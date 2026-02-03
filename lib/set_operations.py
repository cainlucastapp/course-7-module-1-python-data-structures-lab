# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # Use set comprehension to extract unique majors from student records
    majors = {
        # Extract the major field from each student tuple
        student[2]
        # Loop through each student in the student_list
        for student in student_list
    }
    
    # Return the set of unique majors
    return majors