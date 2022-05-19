# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# For example: records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# Output:
# alpha
# beta

if __name__ == '__main__':
    sol = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        # creating new list, which goes into the nested list.
        temp = [name, score]
        sol.append(temp)
    
    # creating a set for scores. this makes it easier to return the second lowest number
    # sorting it in ascending order
    score = sorted({s[1] for s in sol})
    # sets cannot be accessed by index etc. that's why I need to convert it into a list.
    score_as_list = list(score)
    second_lowest_score = score_as_list[1] #second index is the searched number.
    
    # returning every name where the number equals the second lowest score variable.
    # since this needs to be sorted, just use the sorted() method.
    solution = sorted([x[0] for x in sol if x[1] == second_lowest_score])
    
    # print with enter '\n' - every name will be printed in a listed form not next to each other.
    print("\n".join(solution))
            
