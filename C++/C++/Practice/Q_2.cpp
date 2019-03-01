//Q2: Find the sum of the 10 positive integers entered by the user if the user enters negative
//    number the loop should be terminated and the result should be displayed.

#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
  int i = 0;
  int a = 0;
  int num;
  while ( i < 10) {
    cout << "enter a number"<< endl;
    cin>>num;
    if (num < 0 )
      break;
    else  {
      a = a + num;
      i = i + 1;
    }
  }
  cout<< a<<endl;
  return 0;
}
