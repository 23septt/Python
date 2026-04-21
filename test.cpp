#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(nullptr)->sync_with_stdio(0);
    string x;
    cin >> x;
    stack<char> stk;
    bool first = true;
    for(auto i : x){
        if(!stk.empty() && stk.top()=='(' && i == ')'){
            stk.pop();
        }
        else{
            stk.push(i);
            }
    }
    cout << stk.size();
}

