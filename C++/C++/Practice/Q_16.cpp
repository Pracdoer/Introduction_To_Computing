//Q15:


#include <iostream>
using namespace std;

int main()  {
    int a = 5;
 
    for(int i = 0; i < a; i++)  {
         for( int j = a; j >= i; j--)  {
              cout<<" ";
        
         }
        
         for (int m = 1; m <= i;  m++)  {
        
              cout<<"*";
         }

    cout<<endl;

    }
    
    return 0;
} 
