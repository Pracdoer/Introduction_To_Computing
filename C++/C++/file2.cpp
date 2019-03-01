#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
   
   int a;
   cout<<"for men type 1, for man type 0" <<endl;
   cin>>a;
   switch(a) {
   
    case 1:
       float Body_fat_percentage;
       float Body_fat;
       float B; 
       float forearm;
       float hip;
       float wrist1;
       float wrist2;
       float wieght;
       float A1;
       float A2;
       float A3;
       float A4;
       float A5;
       cout<<"your body wieght"<<endl;
       cin>>wieght;
       A1 = (wieght * 0.732) + 8.987;
       cout<< "your wrist at fullest point "<<endl;
       cin>> wrist;
       A2 = wrist1 / 3.140;
       cout<< "your wrist at navel"<<endl;
       cin>>wrist2;
       A3 = wrist2 * 0.157;
       cout<<"hip at fullest point"<<endl;
       cin>>hip;
       A4 = hip * 0.249;
       cout<<"forearm at fullest point"<<endl;
       cin>>forearm;
       A5 = forearm * 0.434;
       B = (A1 + A2) - ( A3 + A4) + A5;
       Body_fat = (wieght - B);
       Body_fat_percentage = body_fat * (100 / wieght);
       cout<<Body_fat_percentage<<"  " << Body_fat<<endl;
       break;


       case 0:
       cout<<"enduff";
       break;
 }


 return 0;
}

