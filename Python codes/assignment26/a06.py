## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(x):
    x = round(x)
    x = int(x) 
    i = 0
    while i< x:
        i = i + 1
        if x%i == 0:
            if is_prime(i):
                print i
def is_prime(x): 
    if x >= 2:
        a=int(x)
        if a==x:
            for y in range(2,a):
                if not ( a % y ):
                    return False
        else:
	    return False
        return True
        return False
#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(x):
    count = 0
    num = 0
    if type(x) == (float):
        return None
    while count != x:
        if is_prime(num):
            count = count + 1
        num = num + 1
    if count == float:
        return None
    if count == x:
        return num - 1

#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
