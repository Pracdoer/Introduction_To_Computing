//Q21: Write a function named "sum_from_to" that takes two integer arguments, call them "first" and
//    "last", and returns as its value the sum of all the integers between first and last inclusive. Thus,
//     for example, cout << sum_from_to(4,7) << endl;//will print 22 because 4+5+6+7 = 22
//     cout << sum_from_to(-3,1) << endl;//will print -5 'cause (-3)+(-2)+(-1)+0+1 = -5 cout <<
//     sum_from_to(7,4) << endl;// will print 22 because 7+6+5+4 = 22
//     cout << sum_from_to(9,9) << endl;// will print 9




#include<iostream>
using namespace std;

int sum_from_to(int first, int last)  {
     
      cout<<"This fun returns as its value the sum of all the integers between first and last inclusive"<<endl;
  
      int sum = 0;
  
      if (first > last) {
           int change;
           change = first - last;
           first = last;
           last = last + change;
      }
    
      for(int i = first; i <= last; i++)  {
           sum= sum + i;  
      }
  
      return sum;
}

int main() {
      int a;
      int b;
      cout<<"enter first value:"<<endl;
      cin>>a;
   
      cout<<"enter last value:"<<endl;
      cin>>b;
    
      cout<<sum_from_to(a,b)<<endl;
  
      return 0;
}
