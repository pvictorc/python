# Nested Lists problem, it is a simple problem that requires sorting and filtering 
# the input data. The problem is to find the names of students with the second lowest score.
# More didactic approach to solve the problem, using a list of lists and sort.

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a = [score,name]
        students.append(a)
    
    students.sort()
    names = []
    lower=-100000
    qtd=0

    # print(students)
    for i in students:
        
        # print(i[0])
        if i[0] > lower:
            lower = i[0]
            qtd+=1
            # print("lower",lower)
        if qtd==2:
            names.append(i[1])
        if qtd>2:
            break
    names.sort()
    
    # print(names)

    for i in names:
        print(i)