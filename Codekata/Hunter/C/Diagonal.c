#include <stdio.h>
void main()
{
    int a[1000][1000],i,n,j,sum;
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for (i=0;i<n;i++)
    {
        sum = sum + a[i][i];
    }
    printf("%d",sum);
}