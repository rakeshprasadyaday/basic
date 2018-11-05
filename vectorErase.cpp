#include <cmath>
#include <cstdio>
#include <vector>
#include<string>
#include<sstream>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string line,itr;
    int n;
    cin>>n;
    
    getline(cin,line,'\n');
    
    string interm;
    vector<int> tokens(n);
    int x;
    int a,b;
    //stringstream for tokenizing the input
    std::stringstream checkl(line);
    int t;
    while(getline(checkl,interm,' '))
    {
        t=stoi(interm);
        tokens.push_back(t);
    }
    cout<<endl;
    
    cin>>x;
    cout<<endl;
    cin>>a>>b;
    //erase the elements in vector
    tokens.erase(tokens.begin()+x-1);
    tokens.erase(tokens.begin()+a-1,tokens.begin()+b-1);
    cout<<tokens.size();
    //output the vector element after erasing specific range of location
    for(int i=0;i<tokens.size();i++)
    {
        cout<<tokens[i]<<" ";
    }
    
    
    return 0;
}
