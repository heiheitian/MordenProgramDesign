// question2.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include<iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int *p=new int[5]; 
	/*��ջ�ڴ��д����һ��ָ��һ����ڴ��ָ��p
	�������ȷ���ڶ��з����ڴ�Ĵ�С��int[5]����Ȼ�����
	operator new�����ڴ棬Ȼ�󷵻�����ڴ���׵�ַ����ջ��*/
	delete []p; //��ʱ�ͷŶ��е��ڴ�
	return 0;
}

