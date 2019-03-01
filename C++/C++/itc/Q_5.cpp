#include <iostream> 
using namespace std;

int main()  {
   
   int n;
   cout<<"the numbers are"<<endl;
   for (int i = 1000; i <= 3000; i++)  {

        string str = to_string(i);

        int a = str.length();
        for (int j = 0 ; j < a; j++)  {
                n = int (j) - 48;
             
            if (n % 2 == 0)
     
                 cout<<i<<endl;
         }


   }

   return 0;

}
        
