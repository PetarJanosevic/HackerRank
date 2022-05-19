# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    # Call the searched name, get all the numbers and do the math.
    # getting a list of all of the student's marks
    marks_list = student_marks.get(query_name)
    
    mark_sum = 0
    counter = 0
    for x in marks_list:
        mark_sum += x
        counter += 1
    
    # do the math: sum of marks divided by the amount of marks    
    # tasks wants the solution in 2 places after the decimal.
    print("{:.2f}".format(mark_sum/counter))
