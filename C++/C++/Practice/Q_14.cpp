//Q14: Write a program that calculates factorials.



#include <iostream>
#include <stdio.h>
using namespace std;

long factorial(long num)  {
     long b = 1;
     
     for (int i = 1; i <=num; i++) {
          b = b * i;
     }
  
     cout<<"the factorial of given number is  "<<b<<endl;

     return b;
}

int main()  {
     int num;
    
     cout<<"enter a positive number :"<<endl;
     cin>>num;
  
     cout<<factorial(num)<<endl;

     return 0;
}
