#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <cstdlib>
#include <stdlib.h>
using namespace std;

int main()
{

	// Constants
	double g = 9.82;
	string input = "";

	// Ask for input
	cout << endl;
	cout << "Type g to see the gravitational constant..." << endl;
	while (input != "g")
	{
		cin >> input;
	}

	// Print out the gravitational constant
	cout << endl;
	cout << "The gravitational consant is : " << g << " m/s^2" << endl;
	cout << endl;

	system("pause");

	return 0;
}
