//Q1: Program finds the sum of the first 100 positive integers
//    and also their average
#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
  int sum = 0;
  int average = 0 ;
  int a = 0;
  int n = 100;
  for (int i = 0; i < n; i++)  {
    a = a + 1;
    sum = sum + a;
  }
  cout <<sum<< endl;
  average = sum/a;
  cout << average;
  
  return 0;
}




