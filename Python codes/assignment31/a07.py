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

#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(grades, weights):
     g = []
     if grades == []:
         return 0
     if grades == None:
         return None
     if type(grades) == str:
         return f(grades)
     n = len(grades)
     m = len(weights)
     if n != m:
         return None
     for i in grades:
         v = f(i)
         g.append(v)
     num1 = []
     for i in range(0, len(g)):
         if g[i] == None:
             return None
         num1.append(g[i] * weights[i])
     grades = sum(num1)
     credit_hours = sum(weights)
     return grades/credit_hours


#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(["A+"])
    print calculate_sgpa_weighted(['A+'], [4])
