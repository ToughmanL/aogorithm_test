#include<stdio.h> 
#include<iostream> 
#include<string>
#include<math.h>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include"function.h"

using namespace std; 

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };


int getsum(int i,int j)
    {
        int sum=0;
        while(i){sum+=i%10;i=i/10;}
        while(j){sum+=j%10;j=j/10;}
        return sum;
    }

int Robot(int i,int j,int r,int c,int t,int n,vector<vector<int>> &m)
    {
        int sum=getsum(i,j);
        if(i<r&&i>=0&&j<c&&j>=0&&sum<t&&m[i][j]==1)
        {
            m[i][j]=0;
            n=1+Robot(i,j-1,r,c,t,n,m)+
                Robot(i,j+1,r,c,t,n,m)+
                Robot(i-1,j,r,c,t,n,m)+
                Robot(i+1,j,r,c,t,n,m);
        }
        return n;
    }


int main()
{
	int N;
    cin>>N;
    set<int> n;
    for(int i=0;i<N;i++)
    {
        int m;cin>>m;
        n.insert(m);
    }
	cout<<n(2);
    return 0;
    return 0;
}

//int main()
//{
//
//	string s="akdsjhgfaksadhgfksadjhgjfkds";
//	string t="jhg";
//	int num=0;
//	int i;
//	int j=s.find(t,0);
//	for(int i=0;(i=s.find(t,i))!=string::npos;)
//	{
//		i++;
//		num++;
//	}
//    return 0;
//
//    /*int number=0,rows=5,cols=5,threshold=6;
//    vector<vector<int>> m;
//    for (int i=0;i<rows;i++)
//    {
//        vector<int>l;
//        for(int j=0;j<cols;j++)
//            l.push_back(1);
//        m.push_back(l);
//        l.clear();
//    }
//	int n=0;
//	n=Robot(0,0,rows,cols,threshold,number,m);
//    cout<<n<<endl;*/
//}


