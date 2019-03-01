//Q17: Write a program that asks the user to type a positive integer. When the user types a negative
  //   value the program writes ERROR and asks for another value. When the user types 0 that means
//     that the last value has been typed and the program must write the average of the positive
//     integers. If the number of typed values is zero the program writes 'NO AVERAGE'.




#include<iostream>
using namespace std;

int main() {
     int sum = 0;
     int num;
     int number = 0;
     float average;

     do  {
         
         cout << "enter a positive integer:  "<<endl;
         cin>>num;

         if (num > 0) {
              sum += num;
              number = number + 1;
         }

         else if(num < 0)
              cout << "ERROR";
     }
     while (num != 0);  {

          if (number == 0)
               cout << "No Average";

          else {
               average = sum/number;
               cout <<"The average is:  "<< average <<endl;
          }
     }

     return 0;
}
