#include <iostream>

using namespace std;



void sort3(float x,float y,float z)
{
    float temp=0,ans=0;
    if (x<y && x>z) // This isn't doing anything. There are no braces. 

    temp=x;
    x=y;
    y=temp;

    ans=x;
    x=z;
    z=ans;
}

int main()
{
    float a = 3.2, b = 2.8, c = 0.9;
    sort3 (a, b, c);
    cout<< a << "  "<< b << "  " << c <<endl;
}

