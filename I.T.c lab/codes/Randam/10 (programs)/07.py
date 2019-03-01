def run():
    j = 9
    k = 9
    p = 1
    for i in range(10):
        print " " * k," *" *  i
        k -=1
    while j > 1:
        j -= 1
        print " " * p," *" * j
        p +=1
run()
