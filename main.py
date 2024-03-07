mark1=0
mark2=0
mark3=0
grade=0
grade=0

mark1 = int(input('Enter your first exam: '))
mark2 = int(input('Enter your second exam: '))
mark3 = int(input('Enter your third exam: '))

allthree3 =(mark1+ mark2 +mark3 ) 
allthree = (mark1+ mark2 +mark3 ) / 3

def average(allthree):
    return allthree
def yourgrade(avg):
    if 90 <= avg <= 100:
        return 'A'
    elif 80 <= avg <= 89:
        return 'B'
    elif 70 <= avg <= 79:
        return 'C'
    else:
        return 'd'

grades = allthree
grade = yourgrade(grades)
avg = average(allthree)

print("total is: " + str(allthree3))
print("Average grade is : " + str(avg))
print("You grade : " + str(grade))