#include "stdafx.h"
#include<iostream>
#include<vector>
#include<string>
using namespace std;
#define maxlength 100

void Split(string s,char splitchar1,char splitchar2,char splitchar3,vector<string>& vec)
{
	if(vec.size()>0)
		vec.clear();
	int length=s.length();
	int start=0;
	for(int i=0;i<length;i++)
	{
		if((s[i]==splitchar1||s[i]==splitchar2||s[i]==splitchar3)&&i==0)
			start+=1;
		else if(s[i]==splitchar1||s[i]==splitchar2||s[i]==splitchar3)
		{
			vec.push_back(s.substr(start,i-start));
			start=i+1;
		}
		else if(i==length-1)
			vec.push_back(s.substr(start,i+1-start));
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	cout<<"ÇëÊäÈëurl£º"<<endl;
	string s;
	getline(cin,s);
	vector<string> vec;
	Split(s,'/','.',':',vec);
	for(int i=0;i<vec.size()-1;i++)
	{
		if(vec[i]!="")
			cout<<vec[i]<<",";
	}
	cout<<vec[vec.size()-1]<<endl;
	return 0;
}

