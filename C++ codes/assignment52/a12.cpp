 #include <iostream>
#include <stdlib.h>
using namespace std;


//////// START OF MARKER FOR fib
long value = 0;   // ouput value for Fib
long p_value = 1;  // pervoius value
long n_value = 0;  // next value
long fib(int n) {
    if (n < 2)
        return n;
    else {
         for(int i = 0; i <n; i += 1)   {
             n_value = value + p_value;          // becuase next number is made by adding of pervoius number
             value = p_value;                   // changing value to pervoius value
             p_value = n_value;                //pervoius value in next value 
         }    
    }
    
    return value;                        // output value
}


//////// END OF MARKER



//////// DO NOT MODIFY CODE BEYOND THIS LINE

int main(int argc, char* argv[]) {
    cout << (fib(atoi(argv[1]))) <<endl;
    return 0;
}
