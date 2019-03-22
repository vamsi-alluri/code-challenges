#include <iostream>
using namespace std;

class get
{
	public:
	int sum(int N, int K, int a[])
	{
		int i,s=0;
	
	for (i=0;i<K;i++)
	{
		cout<<a[i];
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
	cout<<N<<" "<<K;
	get g;
	cout<<g.sum(N,K,a);
	return 0;
}
