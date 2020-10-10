arr = dict()
for i in range(int(input())):
    student = input()
    student_mark = student.split()
    arr[student_mark[0]] = [float(student_mark[1]), float(student_mark[2]), float(student_mark[3])]
chose_mark = arr[input()]
total_marks = (chose_mark[0]+ chose_mark[1] + chose_mark[2]) / 3
print("{0:.2f}".format(total_marks))