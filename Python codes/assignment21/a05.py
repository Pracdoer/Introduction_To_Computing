## IMPORTS GO HERE
import logging
logging.basicConfig(level=logging.WARN)
## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
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
    elif x == float:
        logging.error("got error. ")
        return False
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    if x == 0:
        return None
    x = round(x)
    x = int(x)
    i = 0
    logging.info("factors are ", (x))
    while i< x:
        i = i + 1
        if x%i == 0:
            print (i)
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(x):
    if x < 2:
        return None
    if is_prime(x):
        return int(x) 
    else:
        logging.debug("Guess isn't good enough. Improve ...")
        x = int(x) -1
        return get_largest_prime(x)
#### End OF MARKER



if __name__ == '__main__':
    print(is_prime(499))  # should return True

    print (get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
