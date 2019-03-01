def calculate_roots(a,b,c):
    D = b**2 - 4 * (a * c)
    if D > 0:
        return  -b + (b**2 -4*(a*c))**0.5 ,  -b + (b**2 -4*(a*c))**0.5
    if D == 0:
        return  -b + (b**2 -4*(a*c))**0.5
    
    if D <0:
        print "The roots are complex"
        

