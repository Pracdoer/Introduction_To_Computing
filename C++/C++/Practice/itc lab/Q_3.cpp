

#include <iostream>
using namespace std;
    
int main() {
  
  float num = 1;
  float diff = 1.0; 
  double sum = 0;
  
  for(int i = 1; i <= 100; i++) 
      sum = sum + num / i;
  
  cout<<"the Sum of the Series is: " <<sum<<endl;
  
  return 0;
}
