






scale = input("Select scale in string: " )
if scale == 'C':
    temp = input("temp: " )
    F =   (temp * 9/5) + 32 
    print 'The temp in Farhanit is ', F
if scale == 'F':
    temp = input('temp:')
    C = (temp - 32) * 5/9
    print 'The temp in Celsius is', C
