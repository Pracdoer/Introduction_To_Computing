#include <iostream>
using namespace std;

int main()  {

int integers = 0;
int even = 0;
int odd = 0;
int i = 0;

while (i < 10)  {

	cout << "Enter an integer ending with -999: " << endl;
	cin >> integers;


	if (integers % 2 == 0)  {
	      even = even + integers;
	}


	else if (integers % 2 != 0)  {
	      odd = odd + integers;
	}

        i--;
	cout << "The sum of your even integers is: " << even << endl;
	cout << "The sum of your odd integers is: " << odd << endl;
	
return 0;
}
