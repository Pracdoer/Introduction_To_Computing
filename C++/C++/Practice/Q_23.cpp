//Q23: Write a function named "g_c_d" that takes two positive integer arguments and returns as its
//     value the greatest common divisor of those two integers. If the function is passed an argument
//     that is not positive (i.e. Greater than zero), then the function should return the value 0 as a
//     sentinel value to indicate that an error occurred





#include<iostream>
using namespace std;

int g_c_d(int num1, int num2)  {
  
  int c = 0;
   
     if (num1 || num2 < 0) 
         cout<<0<<;
         break;
  
     for (int i = 1; i <= num1 && i <= num2; i++) {
  
         if (num1 % i == 0 && num2 % i == 0) 
             c =  i;
         else
             cout<<"NO common Factor"<<endl;

     }

     
  return c;
}

int main()  {
  
  cout << g_c_d(40,50) << endl;
}
       
