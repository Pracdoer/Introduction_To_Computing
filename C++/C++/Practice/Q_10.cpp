//Q:10  Write a program that calculate power of a number using loops.



#include <iostream>
#include <stdio.h>
using namespace std;

int power(int base , int expo) {
    int b = 1;

    for(int i = 1; i <= expo; i++)
        b = b * base;
  
    cout<<"the power is: "<<b<<endl;
  
    return b;
  }


int main() {

    int a;
    int b;

    cout<<"enter base"<<endl;
    cin>>a;
    
    cout<<"enter exponent"<<endl;
    cin>>b;
  
    cout<<power(a , b)<<endl;

  return 0;
}
