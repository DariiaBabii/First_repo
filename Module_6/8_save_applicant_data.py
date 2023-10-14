def save_applicant_data(source, output):
    with open(output, 'w') as fh:
        for student in source:
            line = f"{student['name']},{student['specialty']},{student['math']},{student['lang']},{student['eng']}\n"
            fh.write(line)