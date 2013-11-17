// question1.cpp : 定义控制台应用程序的入口点。
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
	heiheitian(); //输出0
	heiheitian(); //输出1
	return 0;
}

