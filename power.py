#include<stdio.h>
int main()
{
  int base,exponent;
  long long result=1;
  printf("enter a base number:");
  scanf("%d",&exponent);
  while(exponent!=0):
  {
    result*=base;
    --exponent;
  }
  print("answer=%11d",result);
  return 0;
}  
  
