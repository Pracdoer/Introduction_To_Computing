def vowel_consonant(x):
    
	if x == ('y'):
        	
		return  "the letter is sometimes vowel and sometimes consonant"
    
	if x == ('a') or x == ('e') or x == ('o') or x == ('i') or x == ('u'):
        	
		return  "The letter is a vowel"
    
	else:
        	
		return "The letter is consonant"
   

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




