// Q24:Write a function named "is_prime" that takes a positive integer argument and returns as
//     its value the integer 1 if the argument is prime and returns the integer 0 otherwise.





#include<iostream>
using namespace std;

int is_prime(int num)  {
  
      int i;
      int prime = 0;
      int is_Prime = 1;

      for(i = 2; i <= num / 2; ++i)  {
           if(num % i == 0)  {
                is_Prime = 0;
                break;
           }
      }
    
      if (is_Prime == 1)
           prime = 1;
      
      else
           prime = 0;
        
  
      return prime;
  
}

int main()  {
      int x;
      cout<<"enter a positive number:"<<endl;
      cin>>x;
     
      cout << is_prime(x) << endl;

      return 0;
}
       
