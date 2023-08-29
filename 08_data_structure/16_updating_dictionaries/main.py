# Dictionaries
    # Use index with KEYS and VALUES
    # Accepts strings, integer, float, boolean...

student = {'name': 'Diogo', 'age': 26, 'final_grade': 'A', 'Approval': True}

student['name'] = 'Godofredo'
student.update({'name': 'José', 'final_grade': 'B'})
student.update({'address': 'Rua A'})

del student['Approval']

print(student)
print(student.get('address', 'Does not exist.'))