// question1.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <iostream>
using namespace std;

void heiheitian()
{
	static int i=0;
	cout<<i++<<endl;
}
int _tmain(int argc, _TCHAR* argv[])
{
	heiheitian(); //���0
	heiheitian(); //���1
	return 0;
}

