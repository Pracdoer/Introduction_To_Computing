def f(x):
    if  x == ("A+"):
        return 4.00
    if x == ("A"):
        return 4.00
    if x ==("A-"):
        return 3.67
    if x == ("B+"):
        return 3.33
    if x == ("B"):
        return 3.00
    if x == ("B-"):
        return 2.67
    if x == ("C+"):
        return 2.33
    if x == ("C"):
        return 2.00
    if x == ("C-"):
        return 1.67
    if x == ("D+"):
        return 1.33
    if x == ("D"):
        return 1.00
    if x == ("F"):
        return 0.00
    else:
	return None



def calculate_sgpa(x): 
	if type(x) == str
		grades =  f(x)
		return grades
	num_of_subj == 0   
	n = len(x)

	for num_of_subj in range(num_of_subj, n):
	 	v = x(num_of_subj)
		grades = f(v):
	 	grades = grades + 0
    
        sgpa = grades/num_of_subj

	
	





def calculate_sgpa(x):
    if type(x) == str:
        grades =  f(x)
	return grades
    else:
        n = len(x) 
        i = 0
        for i in x:
            
	    grades = f(i) 
	    grades = grades + 0
        sgpa = grades/n
        return sgpa





## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def f(x):
    if  x == ("A+"):
        return 4.00
    if x == ("A"):
        return 4.00
    if x ==("A-"):
        return 3.67
    if x == ("B+"):
        return 3.33
    if x == ("B"):
        return 3.00
    if x == ("B-"):
        return 2.67
    if x == ("C+"):
        return 2.33
    if x == ("C"):
        return 2.00
    if x == ("C-"):
        return 1.67
    if x == ("D+"):
        return 1.33
    if x == ("D"):
        return 1.00
    if x == ("F"):
        return 0.00
    if x ==(" "):
	return 0.0
    if x == None:
        return None



def calculate_sgpa(x):
    if type(x) == str:
        grades =  f(x)
	return grades
    else:
        n = len(x) 
        i = 0
        for i in x:
        
	    grades = f(i) 
	    grades = grades + 0.0
        sgpa = grades/n

#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###


#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    print calculate_sgpa_weighted(['A+'], [4])






def f(x):
    if  x == ("A+"):
        return 4.00
    if x == ("A"):
        return 4.00
    if x ==("A-"):
        return 3.67
    if x == ("B+"):
        return 3.33
    if x == ("B"):
        return 3.00
    if x == ("B-"):
        return 2.67
    if x == ("C+"):
        return 2.33
    if x == ("C"):
        return 2.00
    if x == ("C-"):
        return 1.67
    if x == ("D+"):
        return 1.33
    if x == ("D"):
        return 1.00
    if x == ("F"):
        return 0.00
    if x == (" "):
        return 0.0
    else:
	    return None

g_value = []

def calculate_sgpa(x):
    if type(x) == str:
        l = f(x)
        return l
    if x == []:
        return 0
    if x == None:
        return None
    else:
        n = len(x) 
        for i in x:
            if f(i) == None:
                return None
            v = f(i)
            g_value.append(v);
            l = sum(g_value)
        sgpa = l/n
        return sgpa




the new list can be made here (first see line 15)


def calculate_sgpa(x):
if type(x) == string
        a = yehan p grade wale function ko call kro
        return a
    elif value is None
        return x
    elif list is empty

        return nothing hint(what is meaning of nothing in math)????
    else:
        no:of subjects in list
        use "For" loop as t0  (pick every element of list)hint:lecture 14 (time 20 - 30 mint in middle) how to use 'for loop in a list only loop not other things
            elif i == None
                return None
            a = call the grade function to get value of indivdual function
            put every coming value to a new list   hint: (you well know how to make a list and you also know how to add a coming value in list by using append
            sum the new list's all values and save it in a new veriable

        sgpa = new veriable /no:of subjects
        return sgpa







def f(x):
    if  x == ("A+"):
        return 4.00
    if x == ("A"):
        return 4.00
    if x ==("A-"):
        return 3.67
    if x == ("B+"):
        return 3.33
    if x == ("B"):
        return 3.00
    if x == ("B-"):
        return 2.67
    if x == ("C+"):
        return 2.33
    if x == ("C"):
        return 2.00
    if x == ("C-"):
        return 1.67
    if x == ("D+"):
        return 1.33
    if x == ("D"):
        return 1.00
    if x == ("F"):
        return 0.00
    if x == (" "):
        return 0.0
    else:
	    return None



def calculate_sgpa(x):
    g_value = []
    if x == []:
        return 0
    if x == None:
        return None    
    if type(x) != str:
        n = len(x) 
        for i in x:
            if f(i) == None:
                return None
            v = f(i)
            g_value.append(v);
            l = sum(g_value)
        sgpa = l/n
        return sgpa
    else:
        l = f(x)
        return l
       
        
calculate_sgpa(['D', 'A', 'C-', 'D+', 'C'])




def find_cumulative_marks(results):
    result = []
    score_of_student = 0
    for i in results:
        roll_no = i[0]
        name = i[1]
        
        score_of_student = 0
        for j in range(2,len(i)):
            score_of_student = score_of_student + i[j]
        
        
        
        new = (roll_no, name, score_of_student)
        result.append(new)
    return result
        
      


find_cumulative_marks([
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ])



def find_cumulative_marks(results):
    result = [] 
    a = []
    score_of_student = 0
    for i in results:    
        roll_no = i[0]
        name = i[1]
        for j in range(2, len(i)):
            score_of_student = score_of_student + 1 
            a.append(i[j])
        for i in range(0,len(a)):
            if a[i] == None:
                a[i] = 0
        new = (roll_no, name, sum(a))
        result.append(new)
    return result


find_cumulative_marks([
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ])


For A pattern

a = 7
b = 0
c = 9
while a > 1:
   print c*' '+'*'*1+b*'  '+'*'*1
   a = a - 1
   b = b + 1
   c = c  - 1
   if a == 3:
       c = c-1
       print c*' '+' * '*4
       b = b + 1
       continue

D pattern

n = 4
while n>1:
    if n == 4:
        print '* '*3
    print '* '*1 + 3*' '+'*'*1
    n -= 1
    if n == 1:
        print '* '*3

6 Pattern        
         
for n in range(1 ,8):
    if n == 7 or n == 4 or n == 1:
        print '* '*4
        continue
    if n == 6 or n == 5:
        print '* '*1 + 3*' ' + ' *'*1
        
  if n == 3 or n ==2:
        print '*' *1



d = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
              "username": "jake",
              "bio": "I work at statefarm",
              "following": False
            }
        }, {
            "slug": "and another article",
            "body": "I'm getting bored",
            "tagList": ["bored", "article"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 20,
            "author": {
              "username": "cap",
              "following": True
            }
        }],
        "tweets": [{
            "body": "See my article on training mules.",
            "author": {
              "username": "jake"
            }
        }]
    }

def get_types_counts(d):
    if d == ({}):
        return 0
    dic = {}
    d.items()
    for k, v in d.items():
        counts = 0
        if d[k] == 1 :
            counts = 1
        if d[k] > 8:
            counts = counts + 1
        dic[k] = counts
    print dic
    
get_types_counts(d)



def get_types_counts(d):
    d.items()
    dic = {}
    counts = 0
    for k, v in d.items():
        if v == []:
            counts = 0
        if v > 1:
            counts = counts + 1
        dic[k] = counts
    print dic

d = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
              "username": "jake",
              "bio": "I work at statefarm",
              "following": False
            }
        }],
        "books": [{
            "body": "See my article on training mules.",
            "author": {
              "username": "jake"
            }
        }],
        "papers": []
    }

get_types_counts(d)

