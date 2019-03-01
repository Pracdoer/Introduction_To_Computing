## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
    result = []
    if results == []:
        return []
    if results == None:
        return None
    for i in results:
        roll_no = i[0]
        name = i[1]
        score_of_student = 0
        for j in i[2:]:
            if j == None:
                score_of_student = score_of_student + 0
            else:    

                score_of_student = score_of_student + j
        new = (roll_no, name, score_of_student)
        result.append(new)
    return result
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
    new_lst = find_cumulative_marks(results)
    top_student = []
    top = []
    toppers =[]
    for i in new_lst:
        for j in i[2:]:
            top.append(j)
        v = max(top)
        k  = 0
    while k<len(new_lst):
            
        if v in new_lst[k]:
            roll_no = new_lst[k][0]
            name = new_lst[k][1]
            value = (roll_no, name)
            toppers.append(value)
        k = k + 1
    if len(toppers) > 1:
        return toppers
    else:
        return value
#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
