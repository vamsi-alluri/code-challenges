#include <iostream>
using namespace std;

class get
{
	private:
	int i,s=0;
	public:
	int sum(int N, int K, int a[])
	{	
	for (i=0;i<K;i++)
	{
		s = s + a[i];
	}
	return s;
	}
};
int main() {
	int N,K,a[10000],i;
	cin>>N;
	cin>>K;
	for (i=0;i<N;i++)
	{
		cin>>a[i];
	}
	get g;
	cout<<g.sum(N,K,a);
	return 0;
}
