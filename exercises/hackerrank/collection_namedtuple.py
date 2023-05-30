# collections.namedtuple() from HackerRank
from collections import namedtuple

n = int( input())
labels = input().split()

id_column = dict()
for i in labels:
    id_column[i]=labels.index(i)

Student = namedtuple( 'Student', labels )
avg = 0
rows = []
for i in range(n):
    data = input().split()

    student = Student(ID= data[id_column['ID']],
            MARKS= int(data[id_column['MARKS']]),
            NAME= data[id_column['NAME']],
            CLASS= data[id_column['CLASS']])

    avg += int(student.MARKS)
    
print( "{:.2f}".format(avg/n) )