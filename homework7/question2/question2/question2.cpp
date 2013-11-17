// question2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int *p=new int[5]; 
	/*在栈内存中存放了一个指向一块堆内存的指针p
	程序会先确定在堆中分配内存的大小（int[5]），然后调用
	operator new分配内存，然后返回这块内存的首地址放入栈中*/
	delete []p; //及时释放堆中的内存
	return 0;
}

