// Быстрая сортировка.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

void qsort(vector<int> &matrix, int row) {
	int a = 0;
	int b = row - 1;
	int p = row / 2;
	++p;
	do {
		while (matrix[a] < matrix[p]) a++;
		while (matrix[b] > matrix[p]) b--;

		if (a <= b) {
			swap(matrix[a], matrix[b]);
			a++; b--;
		}
	} while (a <= b);

	if (b > 0)
		qsort(matrix, b + 1);
	if (row > a)
		qsort(matrix, (row -= a));
}

int main()
{
	vector<int> matrix = { 7,3,5,1,6 };
	int size = matrix.size();
	qsort(matrix, size);
	for (int i : matrix)
		cout << i << endl;
	system("pause");
    return 0;
}

