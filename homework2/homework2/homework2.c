#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void MaxSum(int a[32][32],int rank,int column,int mode)
{
}
int main(int argc,char *argv[])
{
	int i,j,rank,column,mode;
	int a[32][32]={0};
	FILE *fp;
	if(strcmp(argv[1],"/a")==0)
	{
		mode=2;
		if((fp=fopen(argv[2],"r"))==NULL)
	    {
		    printf("Can't open the file!");
		    exit(0);
	    }
	}
	else if(strcmp(argv[1],"/h")==0)
	{
		mode=3;
		if((fp=fopen(argv[2],"r"))==NULL)
	    {
		    printf("Can't open the file!");
		    exit(0);
	    }
	}
	else if(strcmp(argv[1],"/v")==0)
	{
		if(strcmp(argv[2],"/h")==0)
		{
			if(strcmp(argv[3],"/a")==0)
			{
				mode=6;
				if((fp=fopen(argv[4],"r"))==NULL)
	            {
		            printf("Can't open the file!");
		            exit(0);
	            }
			}
			else
			{
				mode=5;
				if((fp=fopen(argv[3],"r"))==NULL)
	            {
		            printf("Can't open the file!");
		            exit(0);
	            }
			}
		}
		else
		{
		    mode=4;
			if((fp=fopen(argv[2],"r"))==NULL)
	        {
		        printf("Can't open the file!");
		        exit(0);
	        }
		}
	}
	else
	{
		mode=1;
		if((fp=fopen(argv[1],"r"))==NULL)
	    {
		    printf("Can't open the file!");
		    exit(0);
	    }
	}
	fscanf(fp,"%d",&rank);
	fscanf(fp,"%d",&column);
	for(i=0;i<rank;i++)
	{
		for(j=0;j<column;j++)
			fscanf(fp,"%d",&a[i][j]);
	}
	MaxSum(a,rank,column,mode);
	return 0;
}