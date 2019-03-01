#include <iostream>
#include <string>
using namespace std;

//it is used like if and else by cheaking conditions and sort it out.
 
/*int main()  {

   int month;
   cout<< "enter a number: "<<endl;
   cin>>month;
   switch(month)  {
  
     case 1:
        cout<< "january"<<endl;
        break;
     case 2:
        cout<<"Febaurary"<<endl;
            break;
     case 3:
       cout<< "March"<<endl;
       break;
     case 4:
       cout<<"April"<<endl;
       break;
     case 5:
       cout<<"May"<<endl;
       break;
   int   case 6:
       cout<<"june"<<endlf;
       break;
     case 7:
       cout<<"july"<<endl;
       break;
 
     case 8:
       cout<<"august"<<endl;
       break;
     case 9:
       cout<<"september"<<endl;
       break;

     case 10:
      cout<<"October"<<endl;
      break;
     case 11:
       cout<<"November"<<endl;
       break;

     case 12:
       cout<<"Descember"<<endl;
       break;
     default:  
       cout<<"Value is out of range"<<endl;
       break;
      
 }   
  return 0;
}
*/

int main()  {
   int a[10];
   int a1[] = {1,2,3,4,5,6,7,8,9,10};
   int len = sizeof(a1) / 4;
   for (int i = 0; i < len; i++)  {
       cout<<a1[i]<<endl;}

return 0;

}
