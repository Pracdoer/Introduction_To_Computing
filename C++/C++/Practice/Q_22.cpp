//Q22: Write a function named "enough" that takes one integer argument, call it "goal" and returns as
//    its value the smallest positive integer n for which 1+2+3+. . . +n is at least equal to goal . Thus,
//    for example,
//    cout << enough(9) << endl; //will print 4 because 1+2+3+4 9 but 1+2+3<9
//    cout << enough(21) << endl;//will print 6 'cause 1+2+ . . .+6 21 but 1+2+ . . . 5<21




#include<iostream>
using namespace std;

int enough(int goal)  {
  
     int achive = 0;
     int near = 0;
  
     for(int i = 1; i <= goal; i++)  {
          achive = achive + i;
    
          if (achive == goal) {
               near = i;
               break;
          }
    
          else if(goal-achive == 1)  {
               near = i;
               break;
          }
     }
  

     return near;
}

int main() {
       int x;
       cout<<"enter a number:"<<endl;
       cin>>x;

       cout << enough(x) << endl;
 
       return 0;
}  
