//Q13: Write a program that as for an integer value from the user and then prints the length of the
//    value using loop.


#include <iostream>
using namespace std;

int main()  {
 
    string a;
    int count = 0;
    int len;
    int b;

    cout<< "enter a number: "<<endl;
    cin>>b;
 
    a = to_string(b);
    len = a.length();
  
    for (int i = 1; i <= len; i++)  {
         count = count + 1;
    }
  
    cout<<"the length of intger is  " << count<<endl;

    return 0;
}
