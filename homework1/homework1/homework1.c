#include<stdio.h>
void MaxSumSonArrays(int a[],int length)
{
	int sum=0,currentsum=0,i;//sum��ʾ������͵����ֵ��currentsum��ʾ��ǰ������ĺ�
	int begin=0,end=0;
	if(a==NULL||length<=0)
		printf("Array Error!\n");//������������Ƿ�Ϸ�
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