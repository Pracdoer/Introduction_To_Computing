#include <iostream>
using namespace std;


int main() {
  for(int i = 1; i<=11; i++) {
    
    
    for(int j = 11; j >=i ; j--)
      cout<<" *";
    cout<<endl;
    for (int k = 1; k <= i; k++) 
       cout<<" ";
 
  }
  return 0;
}
  
