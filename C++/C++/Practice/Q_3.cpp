//Q3:Find the sum of the 10 positive integers entered by the user if the user enters negative
//   number that iteration should be skipped without incrementing the loop control value.

#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
  int i = 0;
  int a = 0;
  int num;
  while ( i < 9) {
    cout << "enter a number"<< endl;
    cin>>num;
    if (num < 0 )  {
      i = i - 1;
      continue;
    }
    else  {
      a = a + num;
      i = i + 1;
    }
  }
  cout<<"the sum is  "<<  a<<endl;

  return 0;
}
