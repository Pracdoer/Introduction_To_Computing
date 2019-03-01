R$D
.c## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(y , p=0.0):
    if y<0.00000:
	return None

    if good_enough(p ,y):
	return p

    else:
	new_guess = improve_guess(p ,y)
	return sqrt(y ,new_guess)

def good_enough(p, y):
    if abs(float(p * p - y)) < 0.00001:
	return True
    else:
	return False


#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(k ,g):
    result = (abs(k + g)/2.00000)
    return result


#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(l , g):
    k = l *  1.0000
    v = g * 1.0000

    if l < 1.00000:
	return k + 5.00000
    else:
    	return average(k ,v/k)


#### End OF MARKER




if __name__ == '__main__':
    print sqrt(36)
