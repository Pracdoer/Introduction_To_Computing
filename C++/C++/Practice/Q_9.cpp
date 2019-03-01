//Q9: Write a program that asks the user to type 10 integers and writes the smallest value.


#include <iostream>
using namespace std;

int main() {
     int a;
     int num;
     int num2;
     
     cout<<"enter a number"<<endl;
     cin>>num;
     a = num;
  
    for (int i = 0; i<8 ; i++)  {
        cout<<"enter a number"<<endl;
        cin>>num2;
        if (num2 < num) 
             num = num2;
    }
    
    cout<< "the smallest value is : "<< num;
  
    return 0;
  
}
