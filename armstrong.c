#include<stdio.h>
#include<math.h>
int main(){
int num,rem,res=0,n=0;
printf("Enter a number");
scanf("%d",&num);
while(num!=0)
{num=num/10;
++n;}
while(num!=0)
{
rem=num%10;
res=res+pow(rem,n);
num=num/10;
}
if(res==num)
printf("%d is an Armstrong number",num);
else
printf("%d is an Armstrong number",num);
return 0;}
