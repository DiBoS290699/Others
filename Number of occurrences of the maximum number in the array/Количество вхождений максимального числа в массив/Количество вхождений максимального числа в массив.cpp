// Количество вхождений максимального числа в массив.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	int A[10] = { 2,7,8,4,8,9,2,5,9,8 };
	int count = 1, x = A[0];
	for (int i = 1; i < 10; ++i) {
		if (x < A[i]) { x = A[i]; count = 1; }
		else if (x == A[i]) ++count;
	}
	cout << "Max chislo: " << x << endl;
	cout << "Chislo vhozhdeniy: " << count << endl;
	system("pause");
    return 0;
}

