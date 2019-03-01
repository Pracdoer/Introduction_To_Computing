#include <iostream>
using namespace std;


int main()  {
     
    
    int sum = 0;

    int n = 333;
    for (int i = 1; i<=n; i++)  {
         
         int mult = 1;
	 if (i%2 != 0)   {

              mult = mult * (i*i*i);
	      sum = sum + mult; 
	   }
 
    }

    cout<<"the sum of given series is: "<<sum<<endl;

   return sum;
}
