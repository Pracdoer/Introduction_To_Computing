//Q_19:


#include <iostream>
using namespace std;


int main() {
    
     int a = 5;

     for (int i = 1; i <= a; i++) {
           cout<<"  ";

           for(int j = a ; j >= i; j--) {
                cout<< " *";
           }
           cout<<endl;
           if (i == 5)  {
            continue; }
            for (int k = 1; k <= i; k++)  
                cout <<" ";
           
  
     }
     
     int b = 6;
     for (int i = 2; i <= b; i++) {

           for(int j = b ; j >= i; j--) {
                cout<<" ";
           }
           if (i == 6)
              continue;
           for (int k = 1; k <= i; k++)  {
                cout <<" *";
           }
  
           cout<<endl;
     }
     
  
     return 0;

}
