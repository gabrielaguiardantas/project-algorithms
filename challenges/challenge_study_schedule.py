def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    students_quantity_by_hour = 0
    for student_permanence in permanence_period:
        a, b = student_permanence
        if type(a) != int or type(b) != int or type(target_time) != int:
            return None
        else:
            if target_time in range(a, b + 1):
                students_quantity_by_hour += 1
    return students_quantity_by_hour
