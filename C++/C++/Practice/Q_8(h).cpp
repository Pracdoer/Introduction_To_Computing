//Q8 : Write a program that asks the user to type 10 integers and write the number of occurrence of the
       //biggest value.



#include <iostream>
using namespace std;


int main() {
  int count = 1;
  int num = 0;
  int num2;
 
  for (int i = 0; i< 10; i++)  {
    cout<<"enter a number"<<endl;
    cin>>num2;
    if (num2 == num) 
        count = count + 1; 
    if (num2 > num)
        num = num2; 
    }

  cout<< "the number of accourance of largest value is : "<< count<<endl;

  return 0;
}
