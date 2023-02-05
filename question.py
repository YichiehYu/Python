#(1)
def roundGrade(grade):
    grade1 = grade+1
    if grade1 >= 40 and grade1 < grade + 3 and grade1 % 5 == 0:
        print(grade1)
        return grade1
    elif grade < 40:
        print(grade)
        return grade
    else:
        pass

    grade2 = grade+2
    if grade >= 40 and grade2 < grade + 3 and grade2 % 5 == 0:
        print(grade2)
        return grade2
    elif grade < 40:
        print(grade)
        return grade
    else:
        pass

#(2)
roundGrade(33)
roundGrade(73)
roundGrade(153)
roundGrade(39)

far = []
high = 100
for i in range (1,11):
    if i == 1:
        far.append(high)
    else:
        far.append(high * 2)
    high = high /2

print(f'經過的總距離: far = {sum(far)}')
print(f'第十次反彈高度:high = {high}')

    #
    # newscore_d = score_d + 1
    # if newscore_d < 40:
    #     pass
    # else:
    #     newscore_d + 1
    #     if score_d < 40 and newscore_d < newscore_d + 3 and newscore_d % 5 == 0:
    #         print(newscore_d)
    #         break