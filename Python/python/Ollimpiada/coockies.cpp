#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <map>

using namespace std;


int main(){ 
    int size;
    cin >> size;
    map<string, int> wordMap;
    int counter = 0;
    int warning = 0;
    for (int i = 0;  i < size; i++){
        string name;
        cin >> name;
        if (wordMap.count(name) > 0){
            wordMap[name] +=1;
        }
        else{
            wordMap[name] = 1;
        }
        counter +=1;

        if (wordMap[name] > 1 && wordMap[name] -1 > counter - wordMap[name]){
            warning +=1;
        }
    } 
    cout <<"\n"<< warning<< endl;
}    
