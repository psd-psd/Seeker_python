def gradingStudents(grades):
    rounded_grade=[]
    for i in grades:
        if i<38:
            rounded_grade.append(i)
        else:
            rem=i%5
            if rem>2:
                rounded_grade.append(i+(5-rem))
            else:
                rounded_grade.append(i)
    return rounded_grade
