if __name__ == '__main__':
    n = int(input())
    
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input().strip()
    
    print("Dictionary : ", student_marks)

    print("{:.2f}".format(sum(student_marks.get(query_name))/len(student_marks.get(query_name)))) # to get Answer like 56.00

