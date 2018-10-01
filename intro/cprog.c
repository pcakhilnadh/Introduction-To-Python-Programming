#include <stdio.h>

int main()
{
int x,*y;
x=8;
y=&x;
x=100;
printf("Y=%d",*y);
return 0;
}
