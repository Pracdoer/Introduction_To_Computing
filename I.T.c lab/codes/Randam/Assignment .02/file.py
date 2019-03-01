1)program for time Notation.

def time1(hours):
    hours = hours - 12
    return hours
def time2(hours):
    hours = hours + 12 
    return hours
def apt(hours):
    if hours < 12:
        v = "am"
        return v
    if hours > 12:
        v = "pm"
        return v

for i in range(0,25):
    hours = int(input("enter Hours in your choose: "))
    minutes = int(input("enter minutes in your chioce: "))
    if hours < 12:
        hours = time2(hours)
        print "hours in 24 Notation is " , hours,":", minutes
        break
    if hours > 12:
        timing = apt(hours)
        hours = time1(hours)
        print "hours in 12 Notation is " , hours,":",minutes, timing
        break
    if hours == 12:
        hours = hours - 12
        print "the time in 24 Notation is", hours,":",minutes
        break
    else: 
        print "the entered number is out of range"

2) program for lowercase vowel.

def lower_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letters in string:
        if letters in vowels:
            count = count + 1
    print count
