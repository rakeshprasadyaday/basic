// C++ code  2D Vector 
// with different no. of columns 
#include<iostream> 
#include<vector> // for 2D vector 
#include<algorithm>
using namespace std; 

bool sizesort(const vector<int>& v1, const vector<int>& v2)
{
    return v1.size()<v2.size();
}

//For descending order we will use 
//return v1.size()>v2.size();

//Driver Function

int main() 
{ 
    //2D dynamic array
	vector<vector<int>> myVector={{1,2},{3,4,5},{6}};
	//Array befor sorting 
	cout<<"The matrix before sorting\n";
	for(int i=0;i<myVector.size();i++)
	{
	    for(int j=0;j<myVector[i].size();j++)
	    {
	        //Print the element of 2D array vector
	        cout<<myVector[i][j]<<" ";
	    }
	    
	    cout<<endl;
	}
//sort function for sorting vector on the basis of number of columns
    sort(myVector.begin(),myVector.end(),sizesort);
	
	//Matrix after sorting the number of elements
	cout<<"Matrix after sorting the number of elements\n";
	for(int i=0;i<myVector.size();i++)
    {
        for(int j=0;j<myVector[i].size();j++)
            {
                cout<<myVector[i][j]<<" ";
                
            }
            
            cout<<endl;
    }
	
	return 0; 

} 
