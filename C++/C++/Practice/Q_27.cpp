#include <iostream>
using namespace std;

float swap_floats(float x , float y)  {

	float c;
        c = x - y;
        y = x;
        x = x - c;
     
       cout<<"x = " << x<<endl;
       cout<<"y = " << y<< endl;

return 0;
}



int main()  {
     float a;
     float b; 
     cout<<"enter float value say x : "<<endl;
     cin>>a;
 
     cout<<"enter float value say y : "<<endl;
     cin>>b;
 
     swap_floats(a,b);

  return 0;
 }

