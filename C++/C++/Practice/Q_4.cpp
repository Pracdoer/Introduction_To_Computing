#include <iostream>
using namespace std;
int main() {
	  
    char c;
    int sum = 0;
    do   {

         cout<< "enter any charckter"<<endl;
	 cin.get(c);
         sum=sum + int(c);
    
    }while(c!=' ');
	cout<< "the sum of ASCI values: " <<sum<<endl;   
    
    return 0;

}
