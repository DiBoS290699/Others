// пузырёк.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>            //необходим для использования функции swap (), sort ()
using namespace std;

int main()
{
	int b, i, j, x, z, A[10] = {4,6,7,2,6,9,4,1,6,8};
	for (i = 0; i < 10; b = 0,  ++i) {
		for (j = 10 - 1; j != 0; (A[j] <= A[j - 1]) ? x = A[j], A[j] = A[j - 1], A[j - 1] = x, b = 1, --j : --j);
		if (!b) break;
	}
	for (z = 0; z < 10; cout << A[z] << ' ', ++z);
	system("pause");
	return 0;
}
//Количество проходов совпадает с количеством элементов в векторе.
//Сначала берётся последний элемент и предыдущий ему,
//int d = c - 1;                           
//они сравниваются, если элемент больше или равен
