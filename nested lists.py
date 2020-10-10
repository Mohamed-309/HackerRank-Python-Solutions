lst = list()
lst_2 = list()
lst_3 = list()
for number in range(int(input())):
    student = input()
    grade = float(input())
    lst.append([student,grade])
for nl in lst:
    lst_2.append(nl[1])
smaller = min(lst_2)
lst_2.remove(smaller)
smaller = min(lst_2)
for nl in lst:
    if smaller in nl:
        lst_3.append(nl[0])
    else:
        continue
fa = lst_3.sort()
for name in lst_3:
    print(name)

