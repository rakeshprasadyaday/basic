
#include<iostream> 
#include<algorithm> // includes all heap operations
using namespace std; 
int main() 
{ 
	for heap operations 
	vector<int> v={20,30,40,25,15};
	make_heap(v.begin(),v.end());
	cout<<"Front Element is "<<v.front()<<endl;
	v.push_back(50);
	//Using push_heap to heapify Elements of the heap
	
	push_heap(v.begin(),v.end());
	cout<<"Front Element after push operations "<<v.front()<<endl;
	
	pop_heap(v.begin(),v.end());
    v.pop_back();
    cout<<"Front Element after Pop operations "<<v.front()<<endl;
    
    //After sorting heap we have
    sort_heap(v.begin(),v.end());
    for(int &x:v)
        cout<<x<<"  ";
    cout<<endl;
    //Checking wether container is heap or not
    is_heap(v.begin(),v.end())?cout<<"The container is heap ": 
    cout<<"The container is not heap ";
    cout<<endl;
	
	
	
	return 0; 
} 
