from collections import namedtuple

num = int(input())
fields = input()

total = 0

for _ in range(num):
    students = namedtuple('student', fields)
    f1, f2, f3, f4 = input().split()
    student = students(f1, f2, f3, f4)
    total += int(student.MARKS)

print('{:.2f}'.format(total / num))
