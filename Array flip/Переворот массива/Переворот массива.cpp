// Переворот массива.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	int i, j, x, n = 11;
	int A[11] = { 0,1,2,3,4,99,6,7,8,9,10 };
	for (i = 0, j = n - 1; i < j; x = A[j], A[j] = A[i], A[i] = x, ++i, --j);
	for (int z = 0; z < n; cout << A[z] << ' ', ++z);
	system("pause");
    return 0;
}