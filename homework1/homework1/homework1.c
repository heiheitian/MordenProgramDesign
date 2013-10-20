#include<stdio.h>
void MaxSumSonArrays(int a[],int length)
{
	int sum=0,currentsum=0,i;//sum表示子数组和的最大值，currentsum表示当前子数组的和
	int begin=0,end=0;
	if(a==NULL||length<=0)
		printf("Array Error!\n");//检测输入数组是否合法
	for(i=0;i<length;i++)
	{
		if(currentsum<=0)
		{
			currentsum=a[i];
			begin=i+1;
		}
		else
			currentsum+=a[i];
		if(currentsum>sum)
		{
			sum=currentsum;
			end=i+1;
		}
	}
	printf("sum=%d:\nfrom: %d to %d\n",sum,begin,end);
}
int main()
{
	int length,i;
	int a[10000]={0};
	scanf("%d",&length);
	for(i=0;i<length;i++)
		scanf("%d",&a[i]);
	MaxSumSonArrays(a,length);
	return 0;
}