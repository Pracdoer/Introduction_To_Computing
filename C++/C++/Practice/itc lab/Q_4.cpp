

#include<iostream>
using namespace std;




int main(){
    
    int m1[3][3], m2[3][3] , result[3][3];
    
    for (int i=0; i<3; i++){
      
        for(int n=0; n<3; n++){
          
            m1[i][n]=n;
            m2[i][n]=n;
            result[i][n] = m1[i][n] * m2[i][n];
            
            cout<<"Multiplication of  "<<m1[i][n]<<"*"<<m2[i][n]<< "   is :  "<<result[i][n]<<endl;
        }
    }


    
    return 0;
}






int main() {

  int m1[3][3];
  int m2[3][3];
  int result[3][3];
  
  for(int i = 0; i < 3; i++)  {
    
    for(int j = 0; j < 3; j++)  
      
      result[i][j] = m1[i][j] * m2[i][j];
      
    
    }
  
  cout<<"The result of multiplication of two Matricx is: "<<result[i][j];

  return 0;
}
