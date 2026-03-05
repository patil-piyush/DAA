#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

void printArray(vector<int> arr)
{
    for(int x : arr)
        cout << x << " ";
    cout << endl;
}

void selectionSort(vector<int>& arr)
{
    int n = arr.size();

    for(int i=0;i<n-1;i++)
    {
        int minIndex=i;

        for(int j=i+1;j<n;j++)
        {
            if(arr[j] < arr[minIndex])
                minIndex=j;
        }

        swap(arr[i],arr[minIndex]);
    }
}

void insertionSort(vector<int>& arr)
{
    int n=arr.size();

    for(int i=1;i<n;i++)
    {
        int key=arr[i];
        int j=i-1;

        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j--;
        }

        arr[j+1]=key;
    }
}

void merge(vector<int>& arr,int left,int mid,int right)
{
    int n1 = mid-left+1;
    int n2 = right-mid;

    vector<int> L(n1),R(n2);

    for(int i=0;i<n1;i++)
        L[i]=arr[left+i];

    for(int j=0;j<n2;j++)
        R[j]=arr[mid+1+j];

    int i=0,j=0,k=left;

    while(i<n1 && j<n2)
    {
        if(L[i]<=R[j])
            arr[k++]=L[i++];
        else
            arr[k++]=R[j++];
    }

    while(i<n1)
        arr[k++]=L[i++];

    while(j<n2)
        arr[k++]=R[j++];
}

void mergeSort(vector<int>& arr,int left,int right)
{
    if(left<right)
    {
        int mid=(left+right)/2;

        mergeSort(arr,left,mid);
        mergeSort(arr,mid+1,right);

        merge(arr,left,mid,right);
    }
}

int partition(vector<int>& arr,int low,int high)
{
    int pivot=arr[high];
    int i=low-1;

    for(int j=low;j<high;j++)
    {
        if(arr[j] < pivot)
        {
            i++;
            swap(arr[i],arr[j]);
        }
    }

    swap(arr[i+1],arr[high]);
    return i+1;
}

void quickSort(vector<int>& arr,int low,int high)
{
    if(low<high)
    {
        int pi=partition(arr,low,high);

        quickSort(arr,low,pi-1);
        quickSort(arr,pi+1,high);
    }
}

int main()
{
    int n;

    cout<<"Enter number of elements: ";
    cin>>n;

    vector<int> arr(n);

    cout<<"Enter elements:\n";

    for(int i=0;i<n;i++)
        cin>>arr[i];

    vector<int> arr1=arr;
    vector<int> arr2=arr;
    vector<int> arr3=arr;
    vector<int> arr4=arr;

    cout<<"\nOriginal Array:\n";
    printArray(arr);

    auto start = high_resolution_clock::now();
    selectionSort(arr1);
    auto end = high_resolution_clock::now();
    cout<<"\nSelection Sort Output:\n";
    printArray(arr1);
    cout<<"Time: "<<duration_cast<microseconds>(end-start).count()<<" microseconds\n";

    start = high_resolution_clock::now();
    insertionSort(arr2);
    end = high_resolution_clock::now();
    cout<<"\nInsertion Sort Output:\n";
    printArray(arr2);
    cout<<"Time: "<<duration_cast<microseconds>(end-start).count()<<" microseconds\n";

    start = high_resolution_clock::now();
    mergeSort(arr3,0,n-1);
    end = high_resolution_clock::now();
    cout<<"\nMerge Sort Output:\n";
    printArray(arr3);
    cout<<"Time: "<<duration_cast<microseconds>(end-start).count()<<" microseconds\n";

    start = high_resolution_clock::now();
    quickSort(arr4,0,n-1);
    end = high_resolution_clock::now();
    cout<<"\nQuick Sort Output:\n";
    printArray(arr4);
    cout<<"Time: "<<duration_cast<microseconds>(end-start).count()<<" microseconds\n";

    return 0;
}