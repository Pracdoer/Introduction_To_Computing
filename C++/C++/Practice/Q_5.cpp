//Q5: Find the sum of the first 10 numbers that are divisible by 3 and 9. if the sum increase than 200 break the loop.


#include <iostream>
using namespace std;

int main() {
  
  int n = 100;
  int b = 0;
  for (int i = 1; i < 100; i++)  {
    if (i % 3 == 0 && i % 9 == 0) {
      b = b + i;
      if (b > 200)  {
        b = b - i;
        break; }
        }
   
  }
  cout <<"the sum of the first 10 numbers that are divisible by 3 and 9 : "<< b ;

  return 0;
}
