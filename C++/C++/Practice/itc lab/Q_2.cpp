

#include <iostream>
using namespace std;

int simpleSum(string str)   {
  
  int multi = 1;
  int sum = 0;
  int l = str.length();
  int array[l];
  
  for (int i = 0; i < l; i++)  {  
    
    array[i] = str[i] - 48 ;
    
  }
  
    
   
  if (array[0] % 2 != 0) {
    
    for(int i = 0; i < l; i++)
    
      sum = sum + array[i];
      
    cout<<"the sum of numbers: " << sum<<endl;
  
  return sum;
  }
  
  
  
  else  {
    
    for(int i = 0; i < l; i++)
        multi = multi * array[i];
  
    cout<<"the multiplication of numbers: " << multi<<endl;
  
  return multi;
  }  


}



int main() {
  
  string str = "2456";
  simpleSum(str);
  return 0;
}
